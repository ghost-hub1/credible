import { chromium } from "playwright";
import fs from "fs-extra";
import crypto from "crypto";
import path from "path";

const OUT_DIR = "./icons";
fs.ensureDirSync(OUT_DIR);

function hash(content) {
  return crypto.createHash("sha1").update(content).digest("hex").slice(0, 12);
}

(async () => {
  const browser = await chromium.launch({
    headless: true,
    args: ["--no-sandbox"],
  });

  const page = await browser.newPage();

  await page.goto("https://credible.com", {
    waitUntil: "networkidle",
    timeout: 120000,
  });

  // Allow React hydration + lazy icons
  await page.waitForTimeout(15000);

  const svgs = await page.evaluate(() => {
    const collected = [];

    document.querySelectorAll("svg").forEach((svg) => {
      const clone = svg.cloneNode(true);

      // Normalize
      clone.removeAttribute("class");
      clone.removeAttribute("style");
      clone.removeAttribute("width");
      clone.removeAttribute("height");

      if (!clone.getAttribute("viewBox")) {
        clone.setAttribute("viewBox", "0 0 24 24");
      }

      collected.push(clone.outerHTML);
    });

    return collected;
  });

  const unique = new Map();
  let saved = 0;

  for (const svg of svgs) {
    const h = hash(svg);
    if (unique.has(h)) continue;

    unique.set(h, true);
    fs.writeFileSync(path.join(OUT_DIR, `credible-icon-${h}.svg`), svg);
    saved++;
  }

  await browser.close();

  console.log(`✔ Extracted ${saved} unique inline SVG icons`);
})();
