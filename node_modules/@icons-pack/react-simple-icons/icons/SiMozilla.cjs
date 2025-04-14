'use strict';

Object.defineProperties(exports, { __esModule: { value: true }, [Symbol.toStringTag]: { value: 'Module' } });

const jsxRuntime = require('react/jsx-runtime');
const React = require('react');

function _interopNamespaceDefault(e) {
  const n = Object.create(null, { [Symbol.toStringTag]: { value: 'Module' } });
  if (e) {
    for (const k in e) {
      if (k !== 'default') {
        const d = Object.getOwnPropertyDescriptor(e, k);
        Object.defineProperty(n, k, d.get ? d : {
          enumerable: true,
          get: () => e[k]
        });
      }
    }
  }
  n.default = e;
  return Object.freeze(n);
}

const React__namespace = /*#__PURE__*/_interopNamespaceDefault(React);

const defaultColor = "#000000";
const SiMozilla = React__namespace.forwardRef(function SiMozilla2({ title = "Mozilla", color = "currentColor", size = 24, ...others }, ref) {
  if (color === "default") {
    color = defaultColor;
  }
  return /* @__PURE__ */ jsxRuntime.jsxs(
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
        /* @__PURE__ */ jsxRuntime.jsx("title", { children: title }),
        /* @__PURE__ */ jsxRuntime.jsx("path", { d: "M0 0v24h24V0zm10.13 6.706c1.481 0 2.858.706 3.352 2.224.565-1.377 1.73-2.224 3.353-2.224 1.87 0 3.565 1.13 3.565 3.564v4.765h1.412v2.26h-4.341v-5.86c0-1.8-.6-2.47-1.765-2.47-1.412 0-1.976 1.024-1.976 2.435V15h1.376v2.259h-4.341v-5.824c0-1.8-.6-2.47-1.765-2.47-1.412 0-1.976 1.024-1.976 2.435V15H9v2.259H2.647V15h1.377V9.176H2.647V6.918H6.99V8.47c.635-1.095 1.693-1.765 3.14-1.765z" })
      ]
    }
  );
});

exports.default = SiMozilla;
exports.defaultColor = defaultColor;
