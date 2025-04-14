
    import * as React from 'react';

    import { IconType } from '../types';

    type SiVercelProps = React.ComponentPropsWithoutRef<'svg'> & {
      /**
       * The title provides an accessible short text description to the SVG
       */
      title?: string;
      /**
       * Hex color or color name or "default" to use the default hex for each icon
       */
      color?: string;
      /**
       * The size of the Icon.
       */
      size?: string | number;
    }

    const defaultColor = '#000000';

    const SiVercel: IconType = React.forwardRef<SVGSVGElement, SiVercelProps>(function SiVercel({title = 'Vercel', color = 'currentColor', size = 24, ...others }, ref) {
      if (color === 'default') {
        color = defaultColor;
      }

      return (
        <svg
          xmlns='http://www.w3.org/2000/svg'
          width={size}
          height={size}
          fill={color}
          viewBox='0 0 24 24'
          ref={ref}
          {...others}
        >
          <title>{title}</title>
          <path d='M24 22.525H0l12-21.05 12 21.05z' />
        </svg>
      );
    });

    export { SiVercel as default, defaultColor };
  