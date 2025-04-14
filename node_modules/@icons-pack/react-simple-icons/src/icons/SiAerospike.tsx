
    import * as React from 'react';

    import { IconType } from '../types';

    type SiAerospikeProps = React.ComponentPropsWithoutRef<'svg'> & {
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

    const defaultColor = '#C22127';

    const SiAerospike: IconType = React.forwardRef<SVGSVGElement, SiAerospikeProps>(function SiAerospike({title = 'Aerospike', color = 'currentColor', size = 24, ...others }, ref) {
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
          <path d='M14.347 15.375 7.45 12.283l6.897-3.072v6.164zM24 0v24H0V0h24zm-4.705 5.386L5.672 11.548l-1.607.743 1.607.688 13.623 6.163v-1.565l-3.576-1.602V8.612l3.576-1.586v-1.64z' />
        </svg>
      );
    });

    export { SiAerospike as default, defaultColor };
  