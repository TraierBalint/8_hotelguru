'use client';
'use strict';

var jsxRuntime = require('react/jsx-runtime');
var core = require('@mantine/core');
var useDatesState = require('../../hooks/use-dates-state/use-dates-state.cjs');
require('dayjs');
require('@mantine/hooks');
require('../DatesProvider/DatesProvider.cjs');
require('react');
var Calendar = require('../Calendar/Calendar.cjs');

const defaultProps = {
  type: "default",
  defaultLevel: "month",
  numberOfColumns: 1
};
const DatePicker = core.factory((_props, ref) => {
  const props = core.useProps("DatePicker", defaultProps, _props);
  const {
    classNames,
    styles,
    vars,
    type,
    defaultValue,
    value,
    onChange,
    __staticSelector,
    getDayProps,
    allowSingleDateInRange,
    allowDeselect,
    onMouseLeave,
    numberOfColumns,
    hideOutsideDates,
    __onDayMouseEnter,
    __onDayClick,
    ...others
  } = props;
  const { onDateChange, onRootMouseLeave, onHoveredDateChange, getControlProps } = useDatesState.useDatesState({
    type,
    level: "day",
    allowDeselect,
    allowSingleDateInRange,
    value,
    defaultValue,
    onChange,
    onMouseLeave
  });
  const { resolvedClassNames, resolvedStyles } = core.useResolvedStylesApi({
    classNames,
    styles,
    props
  });
  return /* @__PURE__ */ jsxRuntime.jsx(
    Calendar.Calendar,
    {
      ref,
      minLevel: "month",
      classNames: resolvedClassNames,
      styles: resolvedStyles,
      __staticSelector: __staticSelector || "DatePicker",
      onMouseLeave: onRootMouseLeave,
      numberOfColumns,
      hideOutsideDates: hideOutsideDates ?? numberOfColumns !== 1,
      __onDayMouseEnter: (_event, date) => {
        onHoveredDateChange(date);
        __onDayMouseEnter?.(_event, date);
      },
      __onDayClick: (_event, date) => {
        onDateChange(date);
        __onDayClick?.(_event, date);
      },
      getDayProps: (date) => ({
        ...getControlProps(date),
        ...getDayProps?.(date)
      }),
      ...others
    }
  );
});
DatePicker.classes = Calendar.Calendar.classes;
DatePicker.displayName = "@mantine/dates/DatePicker";

exports.DatePicker = DatePicker;
//# sourceMappingURL=DatePicker.cjs.map
