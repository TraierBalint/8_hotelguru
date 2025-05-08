'use client';
import { jsx } from 'react/jsx-runtime';
import { factory, useProps, useResolvedStylesApi } from '@mantine/core';
import { useDatesState } from '../../hooks/use-dates-state/use-dates-state.mjs';
import 'dayjs';
import '@mantine/hooks';
import '../DatesProvider/DatesProvider.mjs';
import 'react';
import { Calendar } from '../Calendar/Calendar.mjs';

const defaultProps = {
  type: "default",
  defaultLevel: "month",
  numberOfColumns: 1
};
const DatePicker = factory((_props, ref) => {
  const props = useProps("DatePicker", defaultProps, _props);
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
  const { onDateChange, onRootMouseLeave, onHoveredDateChange, getControlProps } = useDatesState({
    type,
    level: "day",
    allowDeselect,
    allowSingleDateInRange,
    value,
    defaultValue,
    onChange,
    onMouseLeave
  });
  const { resolvedClassNames, resolvedStyles } = useResolvedStylesApi({
    classNames,
    styles,
    props
  });
  return /* @__PURE__ */ jsx(
    Calendar,
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
DatePicker.classes = Calendar.classes;
DatePicker.displayName = "@mantine/dates/DatePicker";

export { DatePicker };
//# sourceMappingURL=DatePicker.mjs.map
