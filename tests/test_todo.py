# tests/test_todo.py

import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch(headless=False)  # headless=Trueにするとブラウザが表示されません
    context = await browser.new_context()
    page = await context.new_page()
    
    # ExpressサーバーのURLを指定
    page_url = "http://localhost:3001"  # Expressサーバーがポート3001の場合
    await page.goto(page_url)
    
    # ToDo追加のテスト
    await page.fill('input[placeholder="Add a new task"]', 'Test Task 1')
    await page.get_by_role('button', name='Add').click()

    
    # ToDoが追加されたことを確認
    todo = page.locator('li', has_text='Test Task 1').first
    assert await todo.is_visible(), "ToDoが追加されていません"
    
    # ToDoの完了をテスト
    await todo.locator('input[type="checkbox"]').check()
    assert await todo.locator('input[type="checkbox"]').is_checked(), "ToDoが完了状態になっていません"
    
    # ToDoの削除をテスト
    await page.get_by_role('button', name='Delete').click()
    # await todo.locator('button.delete-button').click()  # 実際のセレクタに合わせて調整
    assert await page.locator('li >> text=Test Task 1').count() == 0, "ToDoが削除されていません"
    
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())
    print("テストが正常に完了しました。")