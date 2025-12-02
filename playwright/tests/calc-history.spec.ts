import { test, expect } from "@playwright/test";

test("user can perform a calculation and see history and report update", async ({
  page,
}) => {
  await page.goto("/");

  const operand1 = page.locator("#operand1");
  const operand2 = page.locator("#operand2");
  const operation = page.locator("#operation");
  const form = page.locator("#calc-form");
  const resultDisplay = page.locator("#result-display");

  await operand1.fill("5");
  await operand2.fill("3");
  await operation.selectOption("+");

  await form.evaluate((formEl: HTMLFormElement) => formEl.requestSubmit());

  await expect(resultDisplay).toContainText("Result:");

  
  const historyRows = page.locator("#history-table tbody tr");
  await expect(historyRows.first()).toBeVisible();


  const totalCalcs = page.locator("#total-calcs");
  await expect(totalCalcs).not.toHaveText("0");
});



test("invalid operation shows error", async ({ page }) => {
  await page.goto("/");

  
  const response = await page.request.post("/api/calculate", {
    data: {
      operand1: 1,
      operand2: 2,
      operation: "%"
    }
  });

  
  expect(response.status()).toBe(400);

  const body = await response.json();
  expect(body.detail).toBe("Unsupported operation");
});
