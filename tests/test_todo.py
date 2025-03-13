# tests/test_todo.py
import pytest
import asyncio
import os
from playwright.async_api import async_playwright



@pytest.mark.asyncio
async def test_add_todo(page, screenshot_helper):

        # ExpressサーバーのURLを指定
        page_url = "http://localhost:3000"  # Expressサーバーがポート3001の場合
        await page.goto(page_url)        
        await screenshot_helper.capture(page, "goto")

        # ToDo追加のテスト
        await page.fill('input[placeholder="Add a new task"]', 'Test Task 1')
        await page.get_by_role('button', name='Add').click()
        await screenshot_helper.capture(page, "add")

        # ToDoが追加されたことを確認
        todo = page.locator('li', has_text='Test Task 1').first
        assert await todo.is_visible(), "ToDoが追加されていません"
        await screenshot_helper.capture(page, "addedConfirmation")

@pytest.mark.asyncio
async def test_complete_todo(page, screenshot_helper):

        # ExpressサーバーのURLを指定
        page_url = "http://localhost:3000"  # Expressサーバーがポート3001の場合
        await page.goto(page_url)        

        # ToDo追加のテスト（セットアップ）
        await page.fill('input[placeholder="Add a new task"]', 'Test Task 1')
        await page.get_by_role('button', name='Add').click()

        # ToDoが追加されたことを確認
        todo = page.locator('li', has_text='Test Task 1').first
        assert await todo.is_visible(), "ToDoが追加されていません"

        # チェックボックスをクリックしてToDoを完了にする
        checkbox = todo.locator('input[type="checkbox"]')
        await checkbox.click()
        await screenshot_helper.capture(page, "check")

        # チェックが入ったことを確認する
        assert await checkbox.is_checked(), "チェックボックスがチェックされていません"
        await screenshot_helper.capture(page, "checked")

@pytest.mark.asyncio
async def test_delete_todo(page, screenshot_helper):

        # ExpressサーバーのURLを指定
        page_url = "http://localhost:3000"  # Expressサーバーがポート3001の場合
        await page.goto(page_url)        

        # ToDo追加のテスト（セットアップ）
        await page.fill('input[placeholder="Add a new task"]', 'Test Task 1')
        await page.get_by_role('button', name='Add').click()
        await screenshot_helper.capture(page, "beforeDeleted")

        # ToDoが削除されたことを確認
        await page.get_by_role('button', name='Delete').click()
        await screenshot_helper.capture(page, "deleted")
        assert await page.locator('li >> text=Test Task 1').count() == 0, "ToDoが削除されていません"