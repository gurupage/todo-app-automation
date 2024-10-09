# tests/test_todo.py
import pytest
import asyncio
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_add_todo(page):

        # ExpressサーバーのURLを指定
        page_url = "http://localhost:3001"  # Expressサーバーがポート3001の場合
        await page.goto(page_url)        

        # ToDo追加のテスト
        await page.fill('input[placeholder="Add a new task"]', 'Test Task 1')
        await page.get_by_role('button', name='Add').click()

        # ToDoが追加されたことを確認
        todo = page.locator('li', has_text='Test Task 1').first
        assert await todo.is_visible(), "ToDoが追加されていません"

@pytest.mark.asyncio
async def test_complete_todo(page):

        # ExpressサーバーのURLを指定
        page_url = "http://localhost:3001"  # Expressサーバーがポート3001の場合
        await page.goto(page_url)        

        # ToDo追加のテスト（セットアップ）
        await page.fill('input[placeholder="Add a new task"]', 'Test Task 1')
        await page.get_by_role('button', name='Add').click()

        # ToDoが追加されたことを確認
        todo = page.locator('li', has_text='Test Task 1').first
        assert await todo.is_visible(), "ToDoが追加されていません"

@pytest.mark.asyncio
async def test_delete_todo(page):

        # ExpressサーバーのURLを指定
        page_url = "http://localhost:3001"  # Expressサーバーがポート3001の場合
        await page.goto(page_url)        

        # ToDo追加のテスト（セットアップ）
        await page.fill('input[placeholder="Add a new task"]', 'Test Task 1')
        await page.get_by_role('button', name='Add').click()

        # ToDoが削除されたことを確認
        await page.get_by_role('button', name='Delete').click()
        assert await page.locator('li >> text=Test Task 1').count() == 0, "ToDoが削除されていません"