import { jsxs, jsx } from 'react/jsx-runtime';
import * as React from 'react';

const defaultColor = "#0000FF";
const SiDelicious = React.forwardRef(function SiDelicious2({ title = "del.icio.us", color = "currentColor", size = 24, ...others }, ref) {
  if (color === "default") {
    color = defaultColor;
  }
  return /* @__PURE__ */ jsxs(
    "svg",
    {
      xmlns: "http://www.w3.org/2000/svg",
      width: size,
      height: size,
      fill: color,
      viewBox: "0 0 24 24",
      ref,
      ...others,
      children: [
        /* @__PURE__ */ jsx("title", { children: title }),
        /* @__PURE__ */ jsx("path", { d: "M12 12H0v12h12V12zM24 0H12v12h12V0z" })
      ]
    }
  );
});

export { SiDelicious as default, defaultColor };
