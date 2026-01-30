// tools/icon-replacer.js
import fs from "fs";
import path from "path";

const ICON_DIR = "./icons";

const icons = fs
  .readdirSync(ICON_DIR)
  .filter((f) => f.endsWith(".svg"))
  .map((f) => f.replace(".svg", ""));

function replace(file) {
  let html = fs.readFileSync(file, "utf8");

  icons.forEach((icon) => {
    const regex = new RegExp(
      `<([a-z]+)([^>]*class="[^"]*icon-${icon}[^"]*"[^>]*)></\\1>`,
      "g",
    );

    html = html.replace(
      regex,
      `<img src="/icons/${icon}.svg" class="icon-svg" alt="">`,
    );
  });

  fs.writeFileSync(file, html);
}

function walk(dir) {
  fs.readdirSync(dir).forEach((f) => {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) walk(p);
    else if (p.endsWith(".html")) replace(p);
  });
}

walk("./");
console.log("✔ All HTML files rewritten with SVG icons");
