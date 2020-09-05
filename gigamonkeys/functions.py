# Generated from names extracted from https://support.google.com/docs/table/25273

from gigamonkeys.formulas import Function


def DATE(*args) -> Function:
    """
    Converts a provided year, month, and day into a date.
    Learn more: https//support.google.com/docs/answer/3092969
    """
    return Function("DATE", args)


def DATEDIF(*args) -> Function:
    """
    Calculates the number of days, months, or years between two dates.
    Learn more: https//support.google.com/docs/answer/6055612
    """
    return Function("DATEDIF", args)


def DATEVALUE(*args) -> Function:
    """
    Converts a provided date string in a known format to a date value.
    Learn more: https//support.google.com/docs/answer/3093039
    """
    return Function("DATEVALUE", args)


def DAY(*args) -> Function:
    """
    Returns the day of the month that a specific date falls on, in numeric format.
    Learn more: https//support.google.com/docs/answer/3093040
    """
    return Function("DAY", args)


def DAYS(*args) -> Function:
    """
    Returns the number of days between two dates.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061296
    """
    return Function("DAYS", args)


def DAYS360(*args) -> Function:
    """
    Returns the difference between two days based on the 360 day year used in some
    financial interest calculations.
    Learn more: https//support.google.com/docs/answer/3093042
    """
    return Function("DAYS360", args)


def EDATE(*args) -> Function:
    """
    Returns a date a specified number of months before or after another date.
    Learn more: https//support.google.com/docs/answer/3092974
    """
    return Function("EDATE", args)


def EOMONTH(*args) -> Function:
    """
    Returns a date representing the last day of a month which falls a specified
    number of months before or after another date.
    Learn more: https//support.google.com/docs/answer/3093044
    """
    return Function("EOMONTH", args)


def HOUR(*args) -> Function:
    """
    Returns the hour component of a specific time, in numeric format.
    Learn more: https//support.google.com/docs/answer/3093045
    """
    return Function("HOUR", args)


def ISOWEEKNUM(*args) -> Function:
    """
    Returns the number of the ISO week of the year where the provided date falls.
    Learn more: https//support.google.com/docs/answer/7368793
    """
    return Function("ISOWEEKNUM", args)


def MINUTE(*args) -> Function:
    """
    Returns the minute component of a specific time, in numeric format.
    Learn more: https//support.google.com/docs/answer/3093048
    """
    return Function("MINUTE", args)


def MONTH(*args) -> Function:
    """
    Returns the month of the year a specific date falls in, in numeric format.
    Learn more: https//support.google.com/docs/answer/3093052
    """
    return Function("MONTH", args)


def NETWORKDAYS(*args) -> Function:
    """
    Returns the number of net working days between two provided days.
    Learn more: https//support.google.com/docs/answer/3092979
    """
    return Function("NETWORKDAYS", args)


def NETWORKDAYS_INTL(*args) -> Function:
    """
    Returns the number of net working days between two provided days excluding
    specified weekend days and holidays.
    Learn more: https//support.google.com/docs/answer/3295902
    """
    return Function("NETWORKDAYS_INTL", args)


def NOW(*args) -> Function:
    """
    Returns the current date and time as a date value.
    Learn more: https//support.google.com/docs/answer/3092981
    """
    return Function("NOW", args)


def SECOND(*args) -> Function:
    """
    Returns the second component of a specific time, in numeric format.
    Learn more: https//support.google.com/docs/answer/3093054
    """
    return Function("SECOND", args)


def TIME(*args) -> Function:
    """
    Converts a provided hour, minute, and second into a time.
    Learn more: https//support.google.com/docs/answer/3093056
    """
    return Function("TIME", args)


def TIMEVALUE(*args) -> Function:
    """
    Returns the fraction of a 24-hour day the time represents.
    Learn more: https//support.google.com/docs/answer/3267350
    """
    return Function("TIMEVALUE", args)


def TODAY(*args) -> Function:
    """
    Returns the current date as a date value.
    Learn more: https//support.google.com/docs/answer/3092984
    """
    return Function("TODAY", args)


def WEEKDAY(*args) -> Function:
    """
    Returns a number representing the day of the week of the date provided.
    Learn more: https//support.google.com/docs/answer/3092985
    """
    return Function("WEEKDAY", args)


def WEEKNUM(*args) -> Function:
    """
    Returns a number representing the week of the year where the provided date
    falls.
    Learn more: https//support.google.com/docs/answer/3294949
    """
    return Function("WEEKNUM", args)


def WORKDAY(*args) -> Function:
    """
    Calculates the end date after a specified number of working days.
    Learn more: https//support.google.com/docs/answer/3093059
    """
    return Function("WORKDAY", args)


def WORKDAY_INTL(*args) -> Function:
    """
    Calculates the date after a specified number of workdays excluding specified
    weekend days and holidays.
    Learn more: https//support.google.com/docs/answer/3294972
    """
    return Function("WORKDAY_INTL", args)


def YEAR(*args) -> Function:
    """
    Returns the year specified by a given date.
    Learn more: https//support.google.com/docs/answer/3093061
    """
    return Function("YEAR", args)


def YEARFRAC(*args) -> Function:
    """
    Returns the number of years, including fractional years, between two dates using
    a specified day count convention.
    Learn more: https//support.google.com/docs/answer/3092989
    """
    return Function("YEARFRAC", args)


def BIN2DEC(*args) -> Function:
    """
    Converts a signed binary number to decimal format.
    Learn more: https//support.google.com/docs/answer/3092991
    """
    return Function("BIN2DEC", args)


def BIN2HEX(*args) -> Function:
    """
    Converts a signed binary number to signed hexadecimal format.
    Learn more: https//support.google.com/docs/answer/3093133
    """
    return Function("BIN2HEX", args)


def BIN2OCT(*args) -> Function:
    """
    Converts a signed binary number to signed octal format.
    Learn more: https//support.google.com/docs/answer/3092993
    """
    return Function("BIN2OCT", args)


def BITAND(*args) -> Function:
    """
    Bitwise boolean AND of two numbers.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061440
    """
    return Function("BITAND", args)


def BITLSHIFT(*args) -> Function:
    """
    Shifts the bits of the input a certain number of places to the left.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061443
    """
    return Function("BITLSHIFT", args)


def BITOR(*args) -> Function:
    """
    Bitwise boolean OR of 2 numbers.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9083934
    """
    return Function("BITOR", args)


def BITRSHIFT(*args) -> Function:
    """
    Shifts the bits of the input a certain number of places to the right.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9084100
    """
    return Function("BITRSHIFT", args)


def BITXOR(*args) -> Function:
    """
    Bitwise XOR (exclusive OR) of 2 numbers.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9083935
    """
    return Function("BITXOR", args)


def COMPLEX(*args) -> Function:
    """
    Creates a complex number given real and imaginary coefficients.
    Learn more: https//support.google.com/docs/answer/7407888
    """
    return Function("COMPLEX", args)


def DEC2BIN(*args) -> Function:
    """
    Converts a decimal number to signed binary format.
    Learn more: https//support.google.com/docs/answer/3092997
    """
    return Function("DEC2BIN", args)


def DEC2HEX(*args) -> Function:
    """
    Converts a decimal number to signed hexadecimal format.
    Learn more: https//support.google.com/docs/answer/3093137
    """
    return Function("DEC2HEX", args)


def DEC2OCT(*args) -> Function:
    """
    Converts a decimal number to signed octal format.
    Learn more: https//support.google.com/docs/answer/3093138
    """
    return Function("DEC2OCT", args)


def DELTA(*args) -> Function:
    """
    Compare two numeric values, returning 1 if they're equal.
    Learn more: https//support.google.com/docs/answer/3401147
    """
    return Function("DELTA", args)


def ERF(*args) -> Function:
    """
    The ERF function returns the integral of the Gauss error function over an
    interval of values.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9116267.
    """
    return Function("ERF", args)


def ERF_PRECISE(*args) -> Function:
    "See ERF"
    return Function("ERF_PRECISE", args)


def GESTEP(*args) -> Function:
    """
    Returns 1 if the rate is strictly greater than or equal to the provided step
    value or 0 otherwise. If no step value is provided then the default value of 0
    will be used.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061379
    """
    return Function("GESTEP", args)


def HEX2BIN(*args) -> Function:
    """
    Converts a signed hexadecimal number to signed binary format.
    Learn more: https//support.google.com/docs/answer/3093139
    """
    return Function("HEX2BIN", args)


def HEX2DEC(*args) -> Function:
    """
    Converts a signed hexadecimal number to decimal format.
    Learn more: https//support.google.com/docs/answer/3093192
    """
    return Function("HEX2DEC", args)


def HEX2OCT(*args) -> Function:
    """
    Converts a signed hexadecimal number to signed octal format.
    Learn more: https//support.google.com/docs/answer/3093142
    """
    return Function("HEX2OCT", args)


def IMABS(*args) -> Function:
    """
    Returns absolute value of a complex number.
    Learn more: https//support.google.com/docs/answer/7411899
    """
    return Function("IMABS", args)


def IMAGINARY(*args) -> Function:
    """
    Returns the imaginary coefficient of a complex number.
    Learn more: https//support.google.com/docs/answer/7408639
    """
    return Function("IMAGINARY", args)


def IMARGUMENT(*args) -> Function:
    """
    The IMARGUMENT function returns the angle (also known as the argument or \theta)
    of the given complex number in radians.
    Learn more: https//support.google.com/docs/answer/9116360.
    """
    return Function("IMARGUMENT", args)


def IMCONJUGATE(*args) -> Function:
    """
    Returns the complex conjugate of a number.
    Learn more: https//support.google.com/docs/answer/7410791
    """
    return Function("IMCONJUGATE", args)


def IMCOS(*args) -> Function:
    """
    The IMCOS function returns the cosine of the given complex number.
    Learn more: https//support.google.com/docs/answer/9116546.
    """
    return Function("IMCOS", args)


def IMCOSH(*args) -> Function:
    """
    Returns the hyperbolic cosine of the given complex number. For example, a given
    complex number "x+yi" returns "cosh(x+yi)."
    Learn more: https//support.google.com/docs/answer/9366233.
    """
    return Function("IMCOSH", args)


def IMCOT(*args) -> Function:
    """
    Returns the cotangent of the given complex number. For example, a given complex
    number "x+yi" returns "cot(x+yi)."
    Learn more: https//support.google.com/docs/answer/9366254.
    """
    return Function("IMCOT", args)


def IMCOTH(*args) -> Function:
    """
    Returns the hyperbolic cotangent of the given complex number. For example, a
    given complex number "x+yi" returns "coth(x+yi)."
    Learn more: https//support.google.com/docs/answer/9366256.
    """
    return Function("IMCOTH", args)


def IMCSC(*args) -> Function:
    """
    Returns the cosecant of the given complex number.
    Learn more: https//support.google.com/docs/answer/9199155.
    """
    return Function("IMCSC", args)


def IMCSCH(*args) -> Function:
    """
    Returns the hyperbolic cosecant of the given complex number. For example, a
    given complex number "x+yi" returns "csch(x+yi)."
    Learn more: https//support.google.com/docs/answer/9366258.
    """
    return Function("IMCSCH", args)


def IMDIV(*args) -> Function:
    """
    Returns one complex number divided by another.
    Learn more: https//support.google.com/docs/answer/7411898
    """
    return Function("IMDIV", args)


def IMEXP(*args) -> Function:
    """
    Returns Euler's number, e (~2.718) raised to a complex power.
    Learn more: https//support.google.com/docs/answer/9198277.
    """
    return Function("IMEXP", args)


def IMLOG(*args) -> Function:
    """
    Returns the logarithm of a complex number for a specified base.
    Learn more: https//support.google.com/docs/answer/9366486.
    """
    return Function("IMLOG", args)


def IMLOG10(*args) -> Function:
    """
    Returns the logarithm of a complex number with base 10.
    Learn more: https//support.google.com/docs/answer/9366497.
    """
    return Function("IMLOG10", args)


def IMLOG2(*args) -> Function:
    """
    Returns the logarithm of a complex number with base 2.
    Learn more: https//support.google.com/docs/answer/9366426.
    """
    return Function("IMLOG2", args)


def IMPRODUCT(*args) -> Function:
    """
    Returns the result of multiplying a series of complex numbers together.
    Learn more: https//support.google.com/docs/answer/7409679
    """
    return Function("IMPRODUCT", args)


def IMREAL(*args) -> Function:
    """
    Returns the real coefficient of a complex number.
    Learn more: https//support.google.com/docs/answer/7408138
    """
    return Function("IMREAL", args)


def IMSEC(*args) -> Function:
    """
    Returns the secant of the given complex number. For example, a given complex
    number "x+yi" returns "sec(x+yi)."
    Learn more: https//support.google.com/docs/answer/9366728.
    """
    return Function("IMSEC", args)


def IMSECH(*args) -> Function:
    """
    Returns the hyperbolic secant of the given complex number. For example, a given
    complex number "x+yi" returns "sech(x+yi)."
    Learn more: https//support.google.com/docs/answer/9366440.
    """
    return Function("IMSECH", args)


def IMSIN(*args) -> Function:
    """
    Returns the sine of the given complex number.
    Learn more: https//support.google.com/docs/answer/9198962.
    """
    return Function("IMSIN", args)


def IMSINH(*args) -> Function:
    """
    Returns the hyperbolic sine of the given complex number. For example, a given
    complex number "x+yi" returns "sinh(x+yi)."
    Learn more: https//support.google.com/docs/answer/9366445.
    """
    return Function("IMSINH", args)


def IMSUB(*args) -> Function:
    """
    Returns the difference between two complex numbers.
    Learn more: https//support.google.com/docs/answer/7408393
    """
    return Function("IMSUB", args)


def IMSUM(*args) -> Function:
    """
    Returns the sum of a series of complex numbers.
    Learn more: https//support.google.com/docs/answer/7408295
    """
    return Function("IMSUM", args)


def IMTAN(*args) -> Function:
    """
    Returns the tangent of the given complex number.
    Learn more: https//support.google.com/docs/answer/9203334.
    """
    return Function("IMTAN", args)


def IMTANH(*args) -> Function:
    """
    Returns the hyperbolic tangent of the given complex number. For example, a given
    complex number "x+yi" returns "tanh(x+yi)."
    Learn more: https//support.google.com/docs/answer/9366655.
    """
    return Function("IMTANH", args)


def OCT2BIN(*args) -> Function:
    """
    Converts a signed octal number to signed binary format.
    Learn more: https//support.google.com/docs/answer/3093144
    """
    return Function("OCT2BIN", args)


def OCT2DEC(*args) -> Function:
    """
    Converts a signed octal number to decimal format.
    Learn more: https//support.google.com/docs/answer/3093146
    """
    return Function("OCT2DEC", args)


def OCT2HEX(*args) -> Function:
    """
    Converts a signed octal number to signed hexadecimal format.
    Learn more: https//support.google.com/docs/answer/3093147
    """
    return Function("OCT2HEX", args)


def FILTER(*args) -> Function:
    """
    Returns a filtered version of the source range, returning only rows or columns
    which meet the specified conditions.
    Learn more: https//support.google.com/docs/answer/3093197
    """
    return Function("FILTER", args)


def SORT(*args) -> Function:
    """
    Sorts the rows of a given array or range by the values in one or more columns.
    Learn more: https//support.google.com/docs/answer/3093150
    """
    return Function("SORT", args)


def SORTN(*args) -> Function:
    """
    Returns the first n items in a data set after performing a sort.
    Learn more: https//support.google.com/docs/answer/7354624
    """
    return Function("SORTN", args)


def UNIQUE(*args) -> Function:
    """
    Returns unique rows in the provided source range, discarding duplicates. Rows
    are returned in the order in which they first appear in the source range.
    Learn more: https//support.google.com/docs/answer/3093198
    """
    return Function("UNIQUE", args)


def ACCRINT(*args) -> Function:
    """
    Calculates the accrued interest of a security that has periodic payments.
    Learn more: https//support.google.com/docs/answer/3093200
    """
    return Function("ACCRINT", args)


def ACCRINTM(*args) -> Function:
    """
    Calculates the accrued interest of a security that pays interest at maturity.
    Learn more: https//support.google.com/docs/answer/3093202
    """
    return Function("ACCRINTM", args)


def AMORLINC(*args) -> Function:
    """
    Returns the depreciation for an accounting period, or the prorated depreciation
    if the asset was purchased in the middle of a period.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9083932
    """
    return Function("AMORLINC", args)


def COUPDAYBS(*args) -> Function:
    """
    Calculates the number of days from the first coupon, or interest payment, until
    settlement.
    Learn more: https//support.google.com/docs/answer/3093154
    """
    return Function("COUPDAYBS", args)


def COUPDAYS(*args) -> Function:
    """
    Calculates the number of days in the coupon, or interest payment, period that
    contains the specified settlement date.
    Learn more: https//support.google.com/docs/answer/3093204
    """
    return Function("COUPDAYS", args)


def COUPDAYSNC(*args) -> Function:
    """
    Calculates the number of days from the settlement date until the next coupon, or
    interest payment.
    Learn more: https//support.google.com/docs/answer/3093156
    """
    return Function("COUPDAYSNC", args)


def COUPNCD(*args) -> Function:
    """
    Calculates next coupon, or interest payment, date after the settlement date.
    Learn more: https//support.google.com/docs/answer/3093157
    """
    return Function("COUPNCD", args)


def COUPNUM(*args) -> Function:
    """
    Calculates the number of coupons, or interest payments, between the settlement
    date and the maturity date of the investment.
    Learn more: https//support.google.com/docs/answer/3093208
    """
    return Function("COUPNUM", args)


def COUPPCD(*args) -> Function:
    """
    Calculates last coupon, or interest payment, date before the settlement date.
    Learn more: https//support.google.com/docs/answer/3093210
    """
    return Function("COUPPCD", args)


def CUMIPMT(*args) -> Function:
    """
    Calculates the cumulative interest over a range of payment periods for an
    investment based on constant-amount periodic payments and a constant interest
    rate.
    Learn more: https//support.google.com/docs/answer/3093211
    """
    return Function("CUMIPMT", args)


def CUMPRINC(*args) -> Function:
    """
    Calculates the cumulative principal paid over a range of payment periods for an
    investment based on constant-amount periodic payments and a constant interest
    rate.
    Learn more: https//support.google.com/docs/answer/3093159
    """
    return Function("CUMPRINC", args)


def DB(*args) -> Function:
    """
    Calculates the depreciation of an asset for a specified period using the
    arithmetic declining balance method.
    Learn more: https//support.google.com/docs/answer/3093162
    """
    return Function("DB", args)


def DDB(*args) -> Function:
    """
    Calculates the depreciation of an asset for a specified period using the double-
    declining balance method.
    Learn more: https//support.google.com/docs/answer/3093163
    """
    return Function("DDB", args)


def DISC(*args) -> Function:
    """
    Calculates the discount rate of a security based on price.
    Learn more: https//support.google.com/docs/answer/3093216
    """
    return Function("DISC", args)


def DOLLARDE(*args) -> Function:
    """
    Converts a price quotation given as a decimal fraction into a decimal value.
    Learn more: https//support.google.com/docs/answer/3093167
    """
    return Function("DOLLARDE", args)


def DOLLARFR(*args) -> Function:
    """
    Converts a price quotation given as a decimal value into a decimal fraction.
    Learn more: https//support.google.com/docs/answer/3093217
    """
    return Function("DOLLARFR", args)


def DURATION(*args) -> Function:
    """
    Calculates the number of compounding periods required for an investment of a
    specified present value appreciating at a given rate to reach a target value.
    Learn more: https//support.google.com/docs/answer/3093169
    """
    return Function("DURATION", args)


def EFFECT(*args) -> Function:
    """
    Calculates the annual effective interest rate given the nominal rate and number
    of compounding periods per year.
    Learn more: https//support.google.com/docs/answer/3093223
    """
    return Function("EFFECT", args)


def FV(*args) -> Function:
    """
    Calculates the future value of an annuity investment based on constant-amount
    periodic payments and a constant interest rate.
    Learn more: https//support.google.com/docs/answer/3093224
    """
    return Function("FV", args)


def FVSCHEDULE(*args) -> Function:
    """
    Calculates the future value of some principal based on a specified series of
    potentially varying interest rates.
    Learn more: https//support.google.com/docs/answer/3093226
    """
    return Function("FVSCHEDULE", args)


def INTRATE(*args) -> Function:
    """
    Calculates the effective interest rate generated when an investment is purchased
    at one price and sold at another with no interest or dividends generated by the
    investment itself.
    Learn more: https//support.google.com/docs/answer/3093174
    """
    return Function("INTRATE", args)


def IPMT(*args) -> Function:
    """
    Calculates the payment on interest for an investment based on constant-amount
    periodic payments and a constant interest rate.
    Learn more: https//support.google.com/docs/answer/3093175
    """
    return Function("IPMT", args)


def IRR(*args) -> Function:
    """
    Calculates the internal rate of return on an investment based on a series of
    periodic cash flows.
    Learn more: https//support.google.com/docs/answer/3093231
    """
    return Function("IRR", args)


def ISPMT(*args) -> Function:
    """
    The ISPMT function calculates the interest paid during a particular period of an
    investment.
    Learn more: https//support.google.com/docs/answer/9116481.
    """
    return Function("ISPMT", args)


def MDURATION(*args) -> Function:
    """
    Calculates the modified Macaulay duration of a security paying periodic
    interest, such as a US Treasury Bond, based on expected yield.
    Learn more: https//support.google.com/docs/answer/3093178
    """
    return Function("MDURATION", args)


def MIRR(*args) -> Function:
    """
    Calculates the modified internal rate of return on an investment based on a
    series of periodic cash flows and the difference between the interest rate paid
    on financing versus the return received on reinvested income.
    Learn more: https//support.google.com/docs/answer/3093180
    """
    return Function("MIRR", args)


def NOMINAL(*args) -> Function:
    """
    Calculates the annual nominal interest rate given the effective rate and number
    of compounding periods per year.
    Learn more: https//support.google.com/docs/answer/3093234
    """
    return Function("NOMINAL", args)


def NPER(*args) -> Function:
    """
    Calculates the number of payment periods for an investment based on constant-
    amount periodic payments and a constant interest rate.
    Learn more: https//support.google.com/docs/answer/3093183
    """
    return Function("NPER", args)


def NPV(*args) -> Function:
    """
    Calculates the net present value of an investment based on a series of periodic
    cash flows and a discount rate.
    Learn more: https//support.google.com/docs/answer/3093184
    """
    return Function("NPV", args)


def PDURATION(*args) -> Function:
    """
    Returns the number of periods for an investment to reach a specific value at a
    given rate.
    Learn more: https//support.google.com/docs/answer/9368165.
    """
    return Function("PDURATION", args)


def PMT(*args) -> Function:
    """
    Calculates the periodic payment for an annuity investment based on constant-
    amount periodic payments and a constant interest rate.
    Learn more: https//support.google.com/docs/answer/3093185
    """
    return Function("PMT", args)


def PPMT(*args) -> Function:
    """
    Calculates the payment on the principal of an investment based on constant-
    amount periodic payments and a constant interest rate.
    Learn more: https//support.google.com/docs/answer/3093187
    """
    return Function("PPMT", args)


def PRICE(*args) -> Function:
    """
    Calculates the price of a security paying periodic interest, such as a US
    Treasury Bond, based on expected yield.
    Learn more: https//support.google.com/docs/answer/3093188
    """
    return Function("PRICE", args)


def PRICEDISC(*args) -> Function:
    """
    Calculates the price of a discount (non-interest-bearing) security, based on
    expected yield.
    Learn more: https//support.google.com/docs/answer/3093240
    """
    return Function("PRICEDISC", args)


def PRICEMAT(*args) -> Function:
    """
    Calculates the price of a security paying interest at maturity, based on
    expected yield.
    Learn more: https//support.google.com/docs/answer/3093191
    """
    return Function("PRICEMAT", args)


def PV(*args) -> Function:
    """
    Calculates the present value of an annuity investment based on constant-amount
    periodic payments and a constant interest rate.
    Learn more: https//support.google.com/docs/answer/3093243
    """
    return Function("PV", args)


def RATE(*args) -> Function:
    """
    Calculates the interest rate of an annuity investment based on constant-amount
    periodic payments and the assumption of a constant interest rate.
    Learn more: https//support.google.com/docs/answer/3093257
    """
    return Function("RATE", args)


def RECEIVED(*args) -> Function:
    """
    Calculates the amount received at maturity for an investment in fixed-income
    securities purchased on a given date.
    Learn more: https//support.google.com/docs/answer/3093244
    """
    return Function("RECEIVED", args)


def RRI(*args) -> Function:
    """
    Returns the interest rate needed for an investment to reach a specific value
    within a given number of periods.
    Learn more: https//support.google.com/docs/answer/9368238.
    """
    return Function("RRI", args)


def SLN(*args) -> Function:
    """
    Calculates the depreciation of an asset for one period using the straight-line
    method.
    Learn more: https//support.google.com/docs/answer/3093245
    """
    return Function("SLN", args)


def SYD(*args) -> Function:
    """
    Calculates the depreciation of an asset for a specified period using the sum of
    years digits method.
    Learn more: https//support.google.com/docs/answer/3093261
    """
    return Function("SYD", args)


def TBILLEQ(*args) -> Function:
    """
    Calculates the equivalent annualized rate of return of a US Treasury Bill based
    on discount rate.
    Learn more: https//support.google.com/docs/answer/3093249
    """
    return Function("TBILLEQ", args)


def TBILLPRICE(*args) -> Function:
    """
    Calculates the price of a US Treasury Bill based on discount rate.
    Learn more: https//support.google.com/docs/answer/3093251
    """
    return Function("TBILLPRICE", args)


def TBILLYIELD(*args) -> Function:
    """
    Calculates the yield of a US Treasury Bill based on price.
    Learn more: https//support.google.com/docs/answer/3093264
    """
    return Function("TBILLYIELD", args)


def VDB(*args) -> Function:
    """
    Returns the depreciation of an asset for a particular period (or partial
    period).
    Learn more: https//support.google.com/docs/answer/9199424.
    """
    return Function("VDB", args)


def XIRR(*args) -> Function:
    """
    Calculates the internal rate of return of an investment based on a specified
    series of potentially irregularly spaced cash flows.
    Learn more: https//support.google.com/docs/answer/3093266
    """
    return Function("XIRR", args)


def XNPV(*args) -> Function:
    """
    Calculates the net present value of an investment based on a specified series of
    potentially irregularly spaced cash flows and a discount rate.
    Learn more: https//support.google.com/docs/answer/3093268
    """
    return Function("XNPV", args)


def YIELD(*args) -> Function:
    """
    Calculates the annual yield of a security paying periodic interest, such as a US
    Treasury Bond, based on price.
    Learn more: https//support.google.com/docs/answer/3093255
    """
    return Function("YIELD", args)


def YIELDDISC(*args) -> Function:
    """
    Calculates the annual yield of a discount (non-interest-bearing) security, based
    on price.
    Learn more: https//support.google.com/docs/answer/3093270
    """
    return Function("YIELDDISC", args)


def YIELDMAT(*args) -> Function:
    """
    Calculates the annual yield of a security paying interest at maturity, based on
    price.
    Learn more: https//support.google.com/docs/answer/9000132
    """
    return Function("YIELDMAT", args)


def ARRAYFORMULA(*args) -> Function:
    """
    Enables the display of values returned from an array formula into multiple rows
    and/or columns and the use of non-array functions with arrays.
    Learn more: https//support.google.com/docs/answer/3093275
    """
    return Function("ARRAYFORMULA", args)


def DETECTLANGUAGE(*args) -> Function:
    """
    Identifies the language used in text within the specified range.
    Learn more: https//support.google.com/docs/answer/3093278
    """
    return Function("DETECTLANGUAGE", args)


def GOOGLEFINANCE(*args) -> Function:
    """
    Fetches current or historical securities information from Google Finance.
    Learn more: https//support.google.com/docs/answer/3093281
    """
    return Function("GOOGLEFINANCE", args)


def GOOGLETRANSLATE(*args) -> Function:
    """
    Translates text from one language into another
    Learn more: https//support.google.com/docs/answer/3093331
    """
    return Function("GOOGLETRANSLATE", args)


def IMAGE(*args) -> Function:
    """
    Inserts an image into a cell.
    Learn more: https//support.google.com/docs/answer/3093333
    """
    return Function("IMAGE", args)


def QUERY(*args) -> Function:
    """
    Runs a Google Visualization API Query Language query across data.
    Learn more: https//support.google.com/docs/answer/3093343
    """
    return Function("QUERY", args)


def SPARKLINE(*args) -> Function:
    """
    Creates a miniature chart contained within a single cell.
    Learn more: https//support.google.com/docs/answer/3093289
    """
    return Function("SPARKLINE", args)


def ERROR_TYPE(*args) -> Function:
    """
    Returns a number corresponding to the error value in a different cell.
    Learn more: https//support.google.com/docs/answer/3238305
    """
    return Function("ERROR_TYPE", args)


def ISBLANK(*args) -> Function:
    """
    Checks whether the referenced cell is empty.
    Learn more: https//support.google.com/docs/answer/3093290
    """
    return Function("ISBLANK", args)


def ISDATE(*args) -> Function:
    """
    Returns whether a value is a date.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061381
    """
    return Function("ISDATE", args)


def ISEMAIL(*args) -> Function:
    """
    Checks whether a value is a valid email address.
    Learn more: https//support.google.com/docs/answer/3256503
    """
    return Function("ISEMAIL", args)


def ISERR(*args) -> Function:
    """
    Checks whether a value is an error other than `#N/A`.
    Learn more: https//support.google.com/docs/answer/3093348
    """
    return Function("ISERR", args)


def ISERROR(*args) -> Function:
    """
    Checks whether a value is an error.
    Learn more: https//support.google.com/docs/answer/3093349
    """
    return Function("ISERROR", args)


def ISFORMULA(*args) -> Function:
    """
    Checks whether a formula is in the referenced cell.
    Learn more: https//support.google.com/docs/answer/6270316
    """
    return Function("ISFORMULA", args)


def ISLOGICAL(*args) -> Function:
    """
    Checks whether a value is `TRUE` or `FALSE`.
    Learn more: https//support.google.com/docs/answer/3093351
    """
    return Function("ISLOGICAL", args)


def ISNA(*args) -> Function:
    """
    Checks whether a value is the error `#N/A`.
    Learn more: https//support.google.com/docs/answer/3093293
    """
    return Function("ISNA", args)


def ISNONTEXT(*args) -> Function:
    """
    Checks whether a value is non-textual.
    Learn more: https//support.google.com/docs/answer/3093295
    """
    return Function("ISNONTEXT", args)


def ISNUMBER(*args) -> Function:
    """
    Checks whether a value is a number.
    Learn more: https//support.google.com/docs/answer/3093296
    """
    return Function("ISNUMBER", args)


def ISREF(*args) -> Function:
    """
    Checks whether a value is a valid cell reference.
    Learn more: https//support.google.com/docs/answer/3093354
    """
    return Function("ISREF", args)


def ISTEXT(*args) -> Function:
    """
    Checks whether a value is text.
    Learn more: https//support.google.com/docs/answer/3093297
    """
    return Function("ISTEXT", args)


def N(*args) -> Function:
    """
    Returns the argument provided as a number.
    Learn more: https//support.google.com/docs/answer/3093357
    """
    return Function("N", args)


def NA(*args) -> Function:
    """
    Returns the "value not available" error, `#N/A`.
    Learn more: https//support.google.com/docs/answer/3093359
    """
    return Function("NA", args)


def TYPE(*args) -> Function:
    """
    Returns a number associated with the type of data passed into the function.
    Learn more: https//support.google.com/docs/answer/3267375
    """
    return Function("TYPE", args)


def CELL(*args) -> Function:
    """
    Returns the requested information about the specified cell.
    Learn more: https//support.google.com/docs/answer/3267071
    """
    return Function("CELL", args)


def AND(*args) -> Function:
    """
    Returns true if all of the provided arguments are logically true, and false if
    any of the provided arguments are logically false.
    Learn more: https//support.google.com/docs/answer/3093301
    """
    return Function("AND", args)


def FALSE(*args) -> Function:
    """
    Returns the logical value `FALSE`.
    Learn more: https//support.google.com/docs/answer/3093302
    """
    return Function("FALSE", args)


def IF(*args) -> Function:
    """
    Returns one value if a logical expression is `TRUE` and another if it is
    `FALSE`.
    Learn more: https//support.google.com/docs/answer/3093364
    """
    return Function("IF", args)


def IFERROR(*args) -> Function:
    """
    Returns the first argument if it is not an error value, otherwise returns the
    second argument if present, or a blank if the second argument is absent.
    Learn more: https//support.google.com/docs/answer/3093304
    """
    return Function("IFERROR", args)


def IFNA(*args) -> Function:
    """
    Evaluates a value. If the value is an #N/A error, returns the specified value.
    Learn more: https//support.google.com/docs/answer/9365944.
    """
    return Function("IFNA", args)


def IFS(*args) -> Function:
    """
    Evaluates multiple conditions and returns a value that corresponds to the first
    true condition.
    Learn more: https//support.google.com/docs/answer/7014145
    """
    return Function("IFS", args)


def NOT(*args) -> Function:
    """
    Returns the opposite of a logical value - `NOT(TRUE)` returns `FALSE`;
    `NOT(FALSE)` returns `TRUE`.
    Learn more: https//support.google.com/docs/answer/3093305
    """
    return Function("NOT", args)


def OR(*args) -> Function:
    """
    Returns true if any of the provided arguments are logically true, and false if
    all of the provided arguments are logically false.
    Learn more: https//support.google.com/docs/answer/3093306
    """
    return Function("OR", args)


def SWITCH(*args) -> Function:
    """
    Tests an expression against a list of cases and returns the corresponding value
    of the first matching case, with an optional default value if nothing else is
    met.
    Learn more: https//support.google.com/docs/answer/7013690
    """
    return Function("SWITCH", args)


def TRUE(*args) -> Function:
    """
    Returns the logical value `TRUE`.
    Learn more: https//support.google.com/docs/answer/3093307
    """
    return Function("TRUE", args)


def XOR(*args) -> Function:
    """
    The XOR function performs an exclusive or of 2 numbers that returns a 1 if the
    numbers are different, and a 0 otherwise.
    Learn more: https//support.google.com/docs/answer/9116491.
    """
    return Function("XOR", args)


def ADDRESS(*args) -> Function:
    """
    Returns a cell reference as a string.
    Learn more: https//support.google.com/docs/answer/3093308
    """
    return Function("ADDRESS", args)


def CHOOSE(*args) -> Function:
    """
    Returns an element from a list of choices based on index.
    Learn more: https//support.google.com/docs/answer/3093371
    """
    return Function("CHOOSE", args)


def COLUMN(*args) -> Function:
    """
    Returns the column number of a specified cell, with `A=1`.
    Learn more: https//support.google.com/docs/answer/3093373
    """
    return Function("COLUMN", args)


def COLUMNS(*args) -> Function:
    """
    Returns the number of columns in a specified array or range.
    Learn more: https//support.google.com/docs/answer/3093374
    """
    return Function("COLUMNS", args)


def FORMULATEXT(*args) -> Function:
    """
    Returns the formula as a string.
    Learn more: https//support.google.com/docs/answer/9365792.
    """
    return Function("FORMULATEXT", args)


def GETPIVOTDATA(*args) -> Function:
    """
    Extracts an aggregated value from a pivot table that corresponds to the
    specified row and column headings.
    Learn more: https//support.google.com/docs/answer/6167538
    """
    return Function("GETPIVOTDATA", args)


def HLOOKUP(*args) -> Function:
    """
    Horizontal lookup. Searches across the first row of a range for a key and
    returns the value of a specified cell in the column found.
    Learn more: https//support.google.com/docs/answer/3093375
    """
    return Function("HLOOKUP", args)


def INDEX(*args) -> Function:
    """
    Returns the content of a cell, specified by row and column offset.
    Learn more: https//support.google.com/docs/answer/3098242
    """
    return Function("INDEX", args)


def INDIRECT(*args) -> Function:
    """
    Returns a cell reference specified by a string.
    Learn more: https//support.google.com/docs/answer/3093377
    """
    return Function("INDIRECT", args)


def LOOKUP(*args) -> Function:
    """
    Looks through a row or column for a key and returns the value of the cell in a
    result range located in the same position as the search row or column.
    Learn more: https//support.google.com/docs/answer/3256570
    """
    return Function("LOOKUP", args)


def MATCH(*args) -> Function:
    """
    Returns the relative position of an item in a range that matches a specified
    value.
    Learn more: https//support.google.com/docs/answer/3093378
    """
    return Function("MATCH", args)


def OFFSET(*args) -> Function:
    """
    Returns a range reference shifted a specified number of rows and columns from a
    starting cell reference.
    Learn more: https//support.google.com/docs/answer/3093379
    """
    return Function("OFFSET", args)


def ROW(*args) -> Function:
    """
    Returns the row number of a specified cell.
    Learn more: https//support.google.com/docs/answer/3093316
    """
    return Function("ROW", args)


def ROWS(*args) -> Function:
    """
    Returns the number of rows in a specified array or range.
    Learn more: https//support.google.com/docs/answer/3093382
    """
    return Function("ROWS", args)


def VLOOKUP(*args) -> Function:
    """
    Vertical lookup. Searches down the first column of a range for a key and returns
    the value of a specified cell in the row found.
    Learn more: https//support.google.com/docs/answer/3093318
    """
    return Function("VLOOKUP", args)


def ABS(*args) -> Function:
    """
    Returns the absolute value of a number.
    Learn more: https//support.google.com/docs/answer/3093459
    """
    return Function("ABS", args)


def ACOS(*args) -> Function:
    """
    Returns the inverse cosine of a value, in radians.
    Learn more: https//support.google.com/docs/answer/3093461
    """
    return Function("ACOS", args)


def ACOSH(*args) -> Function:
    """
    Returns the inverse hyperbolic cosine of a number.
    Learn more: https//support.google.com/docs/answer/3093391
    """
    return Function("ACOSH", args)


def ACOT(*args) -> Function:
    """
    Returns the inverse cotangent of a value, in radians.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9084227.
    """
    return Function("ACOT", args)


def ACOTH(*args) -> Function:
    """
    Returns the inverse hyperbolic cotangent of a value, in radians. Must not be
    between -1 and 1, inclusive. Learn more.
    """
    return Function("ACOTH", args)


def ASIN(*args) -> Function:
    """
    Returns the inverse sine of a value, in radians.
    Learn more: https//support.google.com/docs/answer/3093464
    """
    return Function("ASIN", args)


def ASINH(*args) -> Function:
    """
    Returns the inverse hyperbolic sine of a number.
    Learn more: https//support.google.com/docs/answer/3093393
    """
    return Function("ASINH", args)


def ATAN(*args) -> Function:
    """
    Returns the inverse tangent of a value, in radians.
    Learn more: https//support.google.com/docs/answer/3093395
    """
    return Function("ATAN", args)


def ATAN2(*args) -> Function:
    """
    Returns the angle between the x-axis and a line segment from the origin (0,0) to
    specified coordinate pair (`x`,`y`), in radians.
    Learn more: https//support.google.com/docs/answer/3093468
    """
    return Function("ATAN2", args)


def ATANH(*args) -> Function:
    """
    Returns the inverse hyperbolic tangent of a number.
    Learn more: https//support.google.com/docs/answer/3093397
    """
    return Function("ATANH", args)


def BASE(*args) -> Function:
    """
    Converts a number into a text representation in another base, for example, base
    2 for binary.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9084167.
    """
    return Function("BASE", args)


def CEILING(*args) -> Function:
    """
    Rounds a number up to the nearest integer multiple of specified significance.
    Learn more: https//support.google.com/docs/answer/3093471
    """
    return Function("CEILING", args)


def CEILING_MATH(*args) -> Function:
    """
    Rounds a number up to the nearest integer multiple of specified significance,
    with negative numbers rounding toward or away from 0 depending on the mode.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061515
    """
    return Function("CEILING_MATH", args)


def CEILING_PRECISE(*args) -> Function:
    """
    Rounds a number up to the nearest integer multiple of specified significance. If
    the number is positive or negative, it is rounded up.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061294
    """
    return Function("CEILING_PRECISE", args)


def COMBIN(*args) -> Function:
    """
    Returns the number of ways to choose some number of objects from a pool of a
    given size of objects.
    Learn more: https//support.google.com/docs/answer/3093400
    """
    return Function("COMBIN", args)


def COMBINA(*args) -> Function:
    """
    Returns the number of ways to choose some number of objects from a pool of a
    given size of objects, including ways that choose the same object multiple
    times.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9084101.
    """
    return Function("COMBINA", args)


def COS(*args) -> Function:
    """
    Returns the cosine of an angle provided in radians.
    Learn more: https//support.google.com/docs/answer/3093476
    """
    return Function("COS", args)


def COSH(*args) -> Function:
    """
    Returns the hyperbolic cosine of any real number.
    Learn more: https//support.google.com/docs/answer/3093477
    """
    return Function("COSH", args)


def COT(*args) -> Function:
    """
    Cotangent of an angle provided in radians.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9084169.
    """
    return Function("COT", args)


def COTH(*args) -> Function:
    """
    Returns the hyperbolic cotangent of any real number.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9084102.
    """
    return Function("COTH", args)


def COUNTBLANK(*args) -> Function:
    """
    Returns the number of empty cells in a given range.
    Learn more: https//support.google.com/docs/answer/3093403
    """
    return Function("COUNTBLANK", args)


def COUNTIF(*args) -> Function:
    """
    Returns a conditional count across a range.
    Learn more: https//support.google.com/docs/answer/3093480
    """
    return Function("COUNTIF", args)


def COUNTIFS(*args) -> Function:
    """
    Returns the count of a range depending on multiple criteria.
    Learn more: https//support.google.com/docs/answer/3256550
    """
    return Function("COUNTIFS", args)


def COUNTUNIQUE(*args) -> Function:
    """
    Counts the number of unique values in a list of specified values and ranges.
    Learn more: https//support.google.com/docs/answer/3093405
    """
    return Function("COUNTUNIQUE", args)


def CSC(*args) -> Function:
    """
    Returns the cosecant of an angle provided in radians.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9084103.
    """
    return Function("CSC", args)


def CSCH(*args) -> Function:
    """
    The CSCH function returns the hyperbolic cosecant of any real number.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9116336.
    """
    return Function("CSCH", args)


def DECIMAL(*args) -> Function:
    """
    The DECIMAL function converts the text representation of a number in another
    base, to base 10 (decimal).
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9116090.
    """
    return Function("DECIMAL", args)


def DEGREES(*args) -> Function:
    """
    Converts an angle value in radians to degrees.
    Learn more: https//support.google.com/docs/answer/3093481
    """
    return Function("DEGREES", args)


def ERFC(*args) -> Function:
    """
    Returns the complementary Gauss error function of a value.
    Learn more: https//support.google.com/docs/answer/3093407
    """
    return Function("ERFC", args)


def ERFC_PRECISE(*args) -> Function:
    "See ERFC"
    return Function("ERFC_PRECISE", args)


def EVEN(*args) -> Function:
    """
    Rounds a number up to the nearest even integer.
    Learn more: https//support.google.com/docs/answer/3093409
    """
    return Function("EVEN", args)


def EXP(*args) -> Function:
    """
    Returns Euler's number, e (~2.718) raised to a power.
    Learn more: https//support.google.com/docs/answer/3093411
    """
    return Function("EXP", args)


def FACT(*args) -> Function:
    """
    Returns the factorial of a number.
    Learn more: https//support.google.com/docs/answer/3093412
    """
    return Function("FACT", args)


def FACTDOUBLE(*args) -> Function:
    """
    Returns the "double factorial" of a number.
    Learn more: https//support.google.com/docs/answer/3093414
    """
    return Function("FACTDOUBLE", args)


def FLOOR(*args) -> Function:
    """
    Rounds a number down to the nearest integer multiple of specified significance.
    Learn more: https//support.google.com/docs/answer/3093487
    """
    return Function("FLOOR", args)


def FLOOR_MATH(*args) -> Function:
    """
    Rounds a number down to the nearest integer multiple of specified significance,
    with negative numbers rounding toward or away from 0 depending on the mode.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061444
    """
    return Function("FLOOR_MATH", args)


def FLOOR_PRECISE(*args) -> Function:
    """
    The FLOOR.PRECISE function rounds a number down to the nearest integer or
    multiple of specified significance.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9116270.
    """
    return Function("FLOOR_PRECISE", args)


def GAMMALN(*args) -> Function:
    """
    Returns the the logarithm of a specified Gamma function, base e (Euler's
    number).
    Learn more: https//support.google.com/docs/answer/3093416
    """
    return Function("GAMMALN", args)


def GAMMALN_PRECISE(*args) -> Function:
    "See GAMMALN"
    return Function("GAMMALN_PRECISE", args)


def GCD(*args) -> Function:
    """
    Returns the greatest common divisor of one or more integers.
    Learn more: https//support.google.com/docs/answer/3093489
    """
    return Function("GCD", args)


def IMLN(*args) -> Function:
    """
    Returns the logarithm of a complex number, base e (Euler's number).
    Learn more: https//support.google.com/docs/answer/9000651
    """
    return Function("IMLN", args)


def IMPOWER(*args) -> Function:
    """
    Returns a complex number raised to a power.
    Learn more: https//support.google.com/docs/answer/9003065
    """
    return Function("IMPOWER", args)


def IMSQRT(*args) -> Function:
    """
    Computes the square root of a complex number.
    Learn more: https//support.google.com/docs/answer/9003168
    """
    return Function("IMSQRT", args)


def INT(*args) -> Function:
    """
    Rounds a number down to the nearest integer that is less than or equal to it.
    Learn more: https//support.google.com/docs/answer/3093490
    """
    return Function("INT", args)


def ISEVEN(*args) -> Function:
    """
    Checks whether the provided value is even.
    Learn more: https//support.google.com/docs/answer/3093419
    """
    return Function("ISEVEN", args)


def ISO_CEILING(*args) -> Function:
    "See CEILING.PRECISE"
    return Function("ISO_CEILING", args)


def ISODD(*args) -> Function:
    """
    Checks whether the provided value is odd.
    Learn more: https//support.google.com/docs/answer/3093491
    """
    return Function("ISODD", args)


def LCM(*args) -> Function:
    """
    Returns the least common multiple of one or more integers.
    Learn more: https//support.google.com/docs/answer/3093421
    """
    return Function("LCM", args)


def LN(*args) -> Function:
    """
    Returns the the logarithm of a number, base e (Euler's number).
    Learn more: https//support.google.com/docs/answer/3093422
    """
    return Function("LN", args)


def LOG(*args) -> Function:
    """
    Returns the the logarithm of a number given a base.
    Learn more: https//support.google.com/docs/answer/3093495
    """
    return Function("LOG", args)


def LOG10(*args) -> Function:
    """
    Returns the the logarithm of a number, base 10.
    Learn more: https//support.google.com/docs/answer/3093423
    """
    return Function("LOG10", args)


def MOD(*args) -> Function:
    """
    Returns the result of the modulo operator, the remainder after a division
    operation.
    Learn more: https//support.google.com/docs/answer/3093497
    """
    return Function("MOD", args)


def MROUND(*args) -> Function:
    """
    Rounds one number to the nearest integer multiple of another.
    Learn more: https//support.google.com/docs/answer/3093426
    """
    return Function("MROUND", args)


def MULTINOMIAL(*args) -> Function:
    """
    Returns the factorial of the sum of values divided by the product of the values'
    factorials.
    Learn more: https//support.google.com/docs/answer/3093429
    """
    return Function("MULTINOMIAL", args)


def MUNIT(*args) -> Function:
    """
    Returns a unit matrix of size dimension x dimension.
    Learn more: https//support.google.com/docs/answer/9368156.
    """
    return Function("MUNIT", args)


def ODD(*args) -> Function:
    """
    Rounds a number up to the nearest odd integer.
    Learn more: https//support.google.com/docs/answer/3093499
    """
    return Function("ODD", args)


def PI(*args) -> Function:
    """
    Returns the value of Pi to 14 decimal places.
    Learn more: https//support.google.com/docs/answer/3093432
    """
    return Function("PI", args)


def POWER(*args) -> Function:
    """
    Returns a number raised to a power.
    Learn more: https//support.google.com/docs/answer/3093433
    """
    return Function("POWER", args)


def PRODUCT(*args) -> Function:
    """
    Returns the result of multiplying a series of numbers together.
    Learn more: https//support.google.com/docs/answer/3093502
    """
    return Function("PRODUCT", args)


def QUOTIENT(*args) -> Function:
    """
    Returns one number divided by another.
    Learn more: https//support.google.com/docs/answer/3093436
    """
    return Function("QUOTIENT", args)


def RADIANS(*args) -> Function:
    """
    Converts an angle value in degrees to radians.
    Learn more: https//support.google.com/docs/answer/3093437
    """
    return Function("RADIANS", args)


def RAND(*args) -> Function:
    """
    Returns a random number between 0 inclusive and 1 exclusive.
    Learn more: https//support.google.com/docs/answer/3093438
    """
    return Function("RAND", args)


def RANDARRAY(*args) -> Function:
    """
    Generates an array of random numbers between 0 and 1.
    Learn more: https//support.google.com/docs/answer/9211904.
    """
    return Function("RANDARRAY", args)


def RANDBETWEEN(*args) -> Function:
    """
    Returns a uniformly random integer between two values, inclusive.
    Learn more: https//support.google.com/docs/answer/3093507
    """
    return Function("RANDBETWEEN", args)


def ROUND(*args) -> Function:
    """
    Rounds a number to a certain number of decimal places according to standard
    rules.
    Learn more: https//support.google.com/docs/answer/3093440
    """
    return Function("ROUND", args)


def ROUNDDOWN(*args) -> Function:
    """
    Rounds a number to a certain number of decimal places, always rounding down to
    the next valid increment.
    Learn more: https//support.google.com/docs/answer/3093442
    """
    return Function("ROUNDDOWN", args)


def ROUNDUP(*args) -> Function:
    """
    Rounds a number to a certain number of decimal places, always rounding up to the
    next valid increment.
    Learn more: https//support.google.com/docs/answer/3093443
    """
    return Function("ROUNDUP", args)


def SEC(*args) -> Function:
    """
    The SEC function returns the secant of an angle, measured in radians.
    Learn more: https//support.google.com/docs/answer/9116395.
    """
    return Function("SEC", args)


def SECH(*args) -> Function:
    """
    The SECH function returns the hyperbolic secant of an angle.
    Learn more: https//support.google.com/docs/answer/9116560
    """
    return Function("SECH", args)


def SEQUENCE(*args) -> Function:
    """
    Returns an array of sequential numbers, such as 1, 2, 3, 4.
    Learn more: https//support.google.com/docs/answer/9368244.
    """
    return Function("SEQUENCE", args)


def SERIESSUM(*args) -> Function:
    """
    Given parameters x, n, m, and a, returns the power series sum a1xn + a2x(n+m) +
    ... + aix(n+(i-1)m), where i is the number of entries in range `a`.
    Learn more: https//support.google.com/docs/answer/3093444
    """
    return Function("SERIESSUM", args)


def SIGN(*args) -> Function:
    """
    Given an input number, returns `-1` if it is negative, `1` if positive, and `0`
    if it is zero.
    Learn more: https//support.google.com/docs/answer/3093513
    """
    return Function("SIGN", args)


def SIN(*args) -> Function:
    """
    Returns the sine of an angle provided in radians.
    Learn more: https//support.google.com/docs/answer/3093447
    """
    return Function("SIN", args)


def SINH(*args) -> Function:
    """
    Returns the hyperbolic sine of any real number.
    Learn more: https//support.google.com/docs/answer/3093517
    """
    return Function("SINH", args)


def SQRT(*args) -> Function:
    """
    Returns the positive square root of a positive number.
    Learn more: https//support.google.com/docs/answer/3093577
    """
    return Function("SQRT", args)


def SQRTPI(*args) -> Function:
    """
    Returns the positive square root of the product of Pi and the given positive
    number.
    Learn more: https//support.google.com/docs/answer/3093579
    """
    return Function("SQRTPI", args)


def SUBTOTAL(*args) -> Function:
    """
    Returns a subtotal for a vertical range of cells using a specified aggregation
    function.
    Learn more: https//support.google.com/docs/answer/3093649
    """
    return Function("SUBTOTAL", args)


def SUM(*args) -> Function:
    """
    Returns the sum of a series of numbers and/or cells.
    Learn more: https//support.google.com/docs/answer/3093669
    """
    return Function("SUM", args)


def SUMIF(*args) -> Function:
    """
    Returns a conditional sum across a range.
    Learn more: https//support.google.com/docs/answer/3093583
    """
    return Function("SUMIF", args)


def SUMIFS(*args) -> Function:
    """
    Returns the sum of a range depending on multiple criteria.
    Learn more: https//support.google.com/docs/answer/3238496
    """
    return Function("SUMIFS", args)


def SUMSQ(*args) -> Function:
    """
    Returns the sum of the squares of a series of numbers and/or cells.
    Learn more: https//support.google.com/docs/answer/3093714
    """
    return Function("SUMSQ", args)


def TAN(*args) -> Function:
    """
    Returns the tangent of an angle provided in radians.
    Learn more: https//support.google.com/docs/answer/3093586
    """
    return Function("TAN", args)


def TANH(*args) -> Function:
    """
    Returns the hyperbolic tangent of any real number.
    Learn more: https//support.google.com/docs/answer/3093755
    """
    return Function("TANH", args)


def TRUNC(*args) -> Function:
    """
    Truncates a number to a certain number of significant digits by omitting less
    significant digits.
    Learn more: https//support.google.com/docs/answer/3093588
    """
    return Function("TRUNC", args)


def ADD(*args) -> Function:
    """
    Returns the sum of two numbers. Equivalent to the `+` operator.
    Learn more: https//support.google.com/docs/answer/3093590
    """
    return Function("ADD", args)


def CONCAT(*args) -> Function:
    """
    Returns the concatenation of two values. Equivalent to the `&` operator.
    Learn more: https//support.google.com/docs/answer/3093592
    """
    return Function("CONCAT", args)


def DIVIDE(*args) -> Function:
    """
    Returns one number divided by another. Equivalent to the `/` operator.
    Learn more: https//support.google.com/docs/answer/3093973
    """
    return Function("DIVIDE", args)


def EQ(*args) -> Function:
    """
    Returns `TRUE` if two specified values are equal and `FALSE` otherwise.
    Equivalent to the `=` operator.
    Learn more: https//support.google.com/docs/answer/3093593
    """
    return Function("EQ", args)


def GT(*args) -> Function:
    """
    Returns `TRUE` if the first argument is strictly greater than the second, and
    `FALSE` otherwise. Equivalent to the `>` operator.
    Learn more: https//support.google.com/docs/answer/3098240
    """
    return Function("GT", args)


def GTE(*args) -> Function:
    """
    Returns `TRUE` if the first argument is greater than or equal to the second, and
    `FALSE` otherwise. Equivalent to the `>=` operator.
    Learn more: https//support.google.com/docs/answer/3093975
    """
    return Function("GTE", args)


def LT(*args) -> Function:
    """
    Returns `TRUE` if the first argument is strictly less than the second, and
    `FALSE` otherwise. Equivalent to the `<` operator.
    Learn more: https//support.google.com/docs/answer/3093596
    """
    return Function("LT", args)


def LTE(*args) -> Function:
    """
    Returns `TRUE` if the first argument is less than or equal to the second, and
    `FALSE` otherwise. Equivalent to the `<=` operator.
    Learn more: https//support.google.com/docs/answer/3093976
    """
    return Function("LTE", args)


def MINUS(*args) -> Function:
    """
    Returns the difference of two numbers. Equivalent to the `-` operator.
    Learn more: https//support.google.com/docs/answer/3093977
    """
    return Function("MINUS", args)


def MULTIPLY(*args) -> Function:
    """
    Returns the product of two numbers. Equivalent to the `*` operator.
    Learn more: https//support.google.com/docs/answer/3093978
    """
    return Function("MULTIPLY", args)


def NE(*args) -> Function:
    """
    Returns `TRUE` if two specified values are not equal and `FALSE` otherwise.
    Equivalent to the `<>` operator.
    Learn more: https//support.google.com/docs/answer/3093981
    """
    return Function("NE", args)


def POW(*args) -> Function:
    """
    Returns a number raised to a power.
    Learn more: https//support.google.com/docs/answer/3093603
    """
    return Function("POW", args)


def UMINUS(*args) -> Function:
    """
    Returns a number with the sign reversed.
    Learn more: https//support.google.com/docs/answer/3093606
    """
    return Function("UMINUS", args)


def UNARY_PERCENT(*args) -> Function:
    """
    Returns a value interpreted as a percentage; that is, `UNARY_PERCENT(100)`
    equals `1`.
    Learn more: https//support.google.com/docs/answer/3093982
    """
    return Function("UNARY_PERCENT", args)


def UPLUS(*args) -> Function:
    """
    Returns a specified number, unchanged.
    Learn more: https//support.google.com/docs/answer/3093608
    """
    return Function("UPLUS", args)


def AVEDEV(*args) -> Function:
    """
    Calculates the average of the magnitudes of deviations of data from a dataset's
    mean.
    Learn more: https//support.google.com/docs/answer/3093613
    """
    return Function("AVEDEV", args)


def AVERAGE(*args) -> Function:
    """
    Returns the numerical average value in a dataset, ignoring text.
    Learn more: https//support.google.com/docs/answer/3093615
    """
    return Function("AVERAGE", args)


def AVERAGE_WEIGHTED(*args) -> Function:
    """
    Finds the weighted average of a set of values, given the values and the
    corresponding weights.
    Learn more: https//support.google.com/docs/answer/9084098.
    """
    return Function("AVERAGE_WEIGHTED", args)


def AVERAGEA(*args) -> Function:
    """
    Returns the numerical average value in a dataset.
    Learn more: https//support.google.com/docs/answer/3093617
    """
    return Function("AVERAGEA", args)


def AVERAGEIF(*args) -> Function:
    """
    Returns the average of a range depending on criteria.
    Learn more: https//support.google.com/docs/answer/3256529
    """
    return Function("AVERAGEIF", args)


def AVERAGEIFS(*args) -> Function:
    """
    Returns the average of a range depending on multiple criteria.
    Learn more: https//support.google.com/docs/answer/3256534
    """
    return Function("AVERAGEIFS", args)


def BETA_DIST(*args) -> Function:
    """
    Returns the probability of a given value as defined by the beta distribution
    function.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9084228.
    """
    return Function("BETA_DIST", args)


def BETA_INV(*args) -> Function:
    """
    Returns the value of the inverse beta distribution function for a given
    probability.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061377
    """
    return Function("BETA_INV", args)


def BETADIST(*args) -> Function:
    "See BETA.DIST."
    return Function("BETADIST", args)


def BETAINV(*args) -> Function:
    "See BETA.INV"
    return Function("BETAINV", args)


def BINOM_DIST(*args) -> Function:
    "See BINOMDIST"
    return Function("BINOM_DIST", args)


def BINOM_INV(*args) -> Function:
    "See CRITBINOM"
    return Function("BINOM_INV", args)


def BINOMDIST(*args) -> Function:
    """
    Calculates the probability of drawing a certain number of successes (or a
    maximum number of successes) in a certain number of tries given a population of
    a certain size containing a certain number of successes, with replacement of
    draws.
    Learn more: https//support.google.com/docs/answer/3093987
    """
    return Function("BINOMDIST", args)


def CHIDIST(*args) -> Function:
    """
    Calculates the right-tailed chi-squared distribution, often used in hypothesis
    testing.
    Learn more: https//support.google.com/docs/answer/7003346
    """
    return Function("CHIDIST", args)


def CHIINV(*args) -> Function:
    """
    Calculates the inverse of the right-tailed chi-squared distribution.
    Learn more: https//support.google.com/docs/answer/7003198
    """
    return Function("CHIINV", args)


def CHISQ_DIST(*args) -> Function:
    """
    Calculates the left-tailed chi-squared distribution, often used in hypothesis
    testing.
    Learn more: https//support.google.com/docs/answer/7003347
    """
    return Function("CHISQ_DIST", args)


def CHISQ_DIST_RT(*args) -> Function:
    """
    Calculates the right-tailed chi-squared distribution, which is commonly used in
    hypothesis testing.
    Learn more: https//support.google.com/docs/answer/7003199
    """
    return Function("CHISQ_DIST_RT", args)


def CHISQ_INV(*args) -> Function:
    """
    Calculates the inverse of the left-tailed chi-squared distribution.
    Learn more: https//support.google.com/docs/answer/7004181
    """
    return Function("CHISQ_INV", args)


def CHISQ_INV_RT(*args) -> Function:
    """
    Calculates the inverse of the right-tailed chi-squared distribution.
    Learn more: https//support.google.com/docs/answer/7003348
    """
    return Function("CHISQ_INV_RT", args)


def CHISQ_TEST(*args) -> Function:
    "See CHITEST"
    return Function("CHISQ_TEST", args)


def CHITEST(*args) -> Function:
    """
    Returns the probability associated with a Pearson’s chi-squared test on the two
    ranges of data. Determines the likelihood that the observed categorical data is
    drawn from an expected distribution.
    Learn more: https//support.google.com/docs/answer/7004263
    """
    return Function("CHITEST", args)


def CONFIDENCE(*args) -> Function:
    "See CONFIDENCE.NORM"
    return Function("CONFIDENCE", args)


def CONFIDENCE_NORM(*args) -> Function:
    """
    Calculates the width of half the confidence interval for a normal distribution.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/3093988.
    """
    return Function("CONFIDENCE_NORM", args)


def CONFIDENCE_T(*args) -> Function:
    """
    Calculates the width of half the confidence interval for a Student’s
    t-distribution.
    Learn more: https//support.google.com/docs/answer/9365672.
    """
    return Function("CONFIDENCE_T", args)


def CORREL(*args) -> Function:
    """
    Calculates r, the Pearson product-moment correlation coefficient of a dataset.
    Learn more: https//support.google.com/docs/answer/3093990
    """
    return Function("CORREL", args)


def COUNT(*args) -> Function:
    """
    Returns a count of the number of numeric values in a dataset.
    Learn more: https//support.google.com/docs/answer/3093620
    """
    return Function("COUNT", args)


def COUNTA(*args) -> Function:
    """
    Returns a count of the number of values in a dataset.
    Learn more: https//support.google.com/docs/answer/3093991
    """
    return Function("COUNTA", args)


def COVAR(*args) -> Function:
    """
    Calculates the covariance of a dataset.
    Learn more: https//support.google.com/docs/answer/3093993
    """
    return Function("COVAR", args)


def COVARIANCE_P(*args) -> Function:
    "See COVAR"
    return Function("COVARIANCE_P", args)


def COVARIANCE_S(*args) -> Function:
    """
    Calculates the covariance of a dataset, where the dataset is a sample of the
    total population.
    Learn more: https//support.google.com/docs/answer/9365675.
    """
    return Function("COVARIANCE_S", args)


def CRITBINOM(*args) -> Function:
    """
    Calculates the smallest value for which the cumulative binomial distribution is
    greater than or equal to a specified criteria.
    Learn more: https//support.google.com/docs/answer/3093623
    """
    return Function("CRITBINOM", args)


def DEVSQ(*args) -> Function:
    """
    Calculates the sum of squares of deviations based on a sample.
    Learn more: https//support.google.com/docs/answer/3093625
    """
    return Function("DEVSQ", args)


def EXPON_DIST(*args) -> Function:
    """
    Returns the value of the exponential distribution function with a specified
    lambda at a specified value.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/3093995.
    """
    return Function("EXPON_DIST", args)


def EXPONDIST(*args) -> Function:
    "See EXPON.DIST"
    return Function("EXPONDIST", args)


def F_DIST(*args) -> Function:
    """
    Calculates the left-tailed F probability distribution (degree of diversity) for
    two data sets with given input x. Alternately called Fisher-Snedecor
    distribution or Snedecor's F distribution.
    Learn more: https//support.google.com/docs/answer/6055706
    """
    return Function("F_DIST", args)


def F_DIST_RT(*args) -> Function:
    """
    Calculates the right-tailed F probability distribution (degree of diversity) for
    two data sets with given input x. Alternately called Fisher-Snedecor
    distribution or Snedecor's F distribution.
    Learn more: https//support.google.com/docs/answer/6055799
    """
    return Function("F_DIST_RT", args)


def F_INV(*args) -> Function:
    """
    Calculates the inverse of the left-tailed F probability distribution. Also
    called the Fisher-Snedecor distribution or Snedecor’s F distribution.
    Learn more: https//support.google.com/docs/answer/7004265
    """
    return Function("F_INV", args)


def F_INV_RT(*args) -> Function:
    """
    Calculates the inverse of the right-tailed F probability distribution. Also
    called the Fisher-Snedecor distribution or Snedecor’s F distribution.
    Learn more: https//support.google.com/docs/answer/7003960
    """
    return Function("F_INV_RT", args)


def F_TEST(*args) -> Function:
    "See FTEST."
    return Function("F_TEST", args)


def FDIST(*args) -> Function:
    "See F.DIST.RT."
    return Function("FDIST", args)


def FINV(*args) -> Function:
    "See F.INV.RT"
    return Function("FINV", args)


def FISHER(*args) -> Function:
    """
    Returns the Fisher transformation of a specified value.
    Learn more: https//support.google.com/docs/answer/3093626
    """
    return Function("FISHER", args)


def FISHERINV(*args) -> Function:
    """
    Returns the inverse Fisher transformation of a specified value.
    Learn more: https//support.google.com/docs/answer/3093998
    """
    return Function("FISHERINV", args)


def FORECAST(*args) -> Function:
    """
    Calculates the expected y-value for a specified x based on a linear regression
    of a dataset.
    Learn more: https//support.google.com/docs/answer/3094000
    """
    return Function("FORECAST", args)


def FORECAST_LINEAR(*args) -> Function:
    "See FORECAST"
    return Function("FORECAST_LINEAR", args)


def FTEST(*args) -> Function:
    """
    Returns the probability associated with an F-test for equality of variances.
    Determines whether two samples are likely to have come from populations with the
    same variance.
    Learn more: https//support.google.com/docs/answer/7004183
    """
    return Function("FTEST", args)


def GAMMA(*args) -> Function:
    """
    Returns the Gamma function evaluated at the specified value.
    Learn more: https//support.google.com/docs/answer/9365856.
    """
    return Function("GAMMA", args)


def GAMMA_DIST(*args) -> Function:
    """
    Calculates the gamma distribution, a two-parameter continuous probability
    distribution.
    Learn more: https//support.google.com/docs/answer/7013990
    """
    return Function("GAMMA_DIST", args)


def GAMMA_INV(*args) -> Function:
    """
    The GAMMA.INV function returns the value of the inverse gamma cumulative
    distribution function for the specified probability and alpha and beta
    parameters.
    Learn more: https//support.google.com/docs/answer/9116467.
    """
    return Function("GAMMA_INV", args)


def GAMMADIST(*args) -> Function:
    "See GAMMA.DIST"
    return Function("GAMMADIST", args)


def GAMMAINV(*args) -> Function:
    "See GAMMA.INV."
    return Function("GAMMAINV", args)


def GAUSS(*args) -> Function:
    """
    The GAUSS function returns the probability that a random variable, drawn from a
    normal distribution, will be between the mean and z standard deviations above
    (or below) the mean.
    Learn more: https//support.google.com/docs/answer/9116278.
    """
    return Function("GAUSS", args)


def GEOMEAN(*args) -> Function:
    """
    Calculates the geometric mean of a dataset.
    Learn more: https//support.google.com/docs/answer/3094001
    """
    return Function("GEOMEAN", args)


def HARMEAN(*args) -> Function:
    """
    Calculates the harmonic mean of a dataset.
    Learn more: https//support.google.com/docs/answer/3094003
    """
    return Function("HARMEAN", args)


def HYPGEOM_DIST(*args) -> Function:
    "See HYPGEOMDIST"
    return Function("HYPGEOM_DIST", args)


def HYPGEOMDIST(*args) -> Function:
    """
    Calculates the probability of drawing a certain number of successes in a certain
    number of tries given a population of a certain size containing a certain number
    of successes, without replacement of draws.
    Learn more: https//support.google.com/docs/answer/3094004
    """
    return Function("HYPGEOMDIST", args)


def INTERCEPT(*args) -> Function:
    """
    Calculates the y-value at which the line resulting from linear regression of a
    dataset will intersect the y-axis (x=0).
    Learn more: https//support.google.com/docs/answer/3093632
    """
    return Function("INTERCEPT", args)


def KURT(*args) -> Function:
    """
    Calculates the kurtosis of a dataset, which describes the shape, and in
    particular the "peakedness" of that dataset.
    Learn more: https//support.google.com/docs/answer/3093634
    """
    return Function("KURT", args)


def LARGE(*args) -> Function:
    """
    Returns the nth largest element from a data set, where n is user-defined.
    Learn more: https//support.google.com/docs/answer/3094008
    """
    return Function("LARGE", args)


def LOGINV(*args) -> Function:
    """
    Returns the value of the inverse log-normal cumulative distribution with given
    mean and standard deviation at a specified value.
    Learn more: https//support.google.com/docs/answer/3094010
    """
    return Function("LOGINV", args)


def LOGNORM_DIST(*args) -> Function:
    "See LOGNORMDIST"
    return Function("LOGNORM_DIST", args)


def LOGNORM_INV(*args) -> Function:
    "See LOGINV"
    return Function("LOGNORM_INV", args)


def LOGNORMDIST(*args) -> Function:
    """
    Returns the value of the log-normal cumulative distribution with given mean and
    standard deviation at a specified value.
    Learn more: https//support.google.com/docs/answer/3094011
    """
    return Function("LOGNORMDIST", args)


def MAX(*args) -> Function:
    """
    Returns the maximum value in a numeric dataset.
    Learn more: https//support.google.com/docs/answer/3094013
    """
    return Function("MAX", args)


def MAXA(*args) -> Function:
    """
    Returns the maximum numeric value in a dataset.
    Learn more: https//support.google.com/docs/answer/3094016
    """
    return Function("MAXA", args)


def MAXIFS(*args) -> Function:
    """
    Returns the maximum value in a range of cells, filtered by a set of criteria.
    Learn more: https//support.google.com/docs/answer/7013817
    """
    return Function("MAXIFS", args)


def MEDIAN(*args) -> Function:
    """
    Returns the median value in a numeric dataset.
    Learn more: https//support.google.com/docs/answer/3094025
    """
    return Function("MEDIAN", args)


def MIN(*args) -> Function:
    """
    Returns the minimum value in a numeric dataset.
    Learn more: https//support.google.com/docs/answer/3094017
    """
    return Function("MIN", args)


def MINA(*args) -> Function:
    """
    Returns the minimum numeric value in a dataset.
    Learn more: https//support.google.com/docs/answer/3094018
    """
    return Function("MINA", args)


def MINIFS(*args) -> Function:
    """
    Returns the minimum value in a range of cells, filtered by a set of criteria.
    Learn more: https//support.google.com/docs/answer/7014063
    """
    return Function("MINIFS", args)


def MODE(*args) -> Function:
    """
    Returns the most commonly occurring value in a dataset.
    Learn more: https//support.google.com/docs/answer/3094029
    """
    return Function("MODE", args)


def MODE_MULT(*args) -> Function:
    """
    Returns the most commonly occurring values in a dataset.
    Learn more: https//support.google.com/docs/answer/9368267.
    """
    return Function("MODE_MULT", args)


def MODE_SNGL(*args) -> Function:
    "See MODE"
    return Function("MODE_SNGL", args)


def NEGBINOM_DIST(*args) -> Function:
    "See NEGBINOMDIST"
    return Function("NEGBINOM_DIST", args)


def NEGBINOMDIST(*args) -> Function:
    """
    Calculates the probability of drawing a certain number of failures before a
    certain number of successes given a probability of success in independent
    trials.
    Learn more: https//support.google.com/docs/answer/3094031
    """
    return Function("NEGBINOMDIST", args)


def NORM_DIST(*args) -> Function:
    "See NORMDIST"
    return Function("NORM_DIST", args)


def NORM_INV(*args) -> Function:
    "See NORMINV"
    return Function("NORM_INV", args)


def NORM_S_DIST(*args) -> Function:
    "See NORMSDIST"
    return Function("NORM_S_DIST", args)


def NORM_S_INV(*args) -> Function:
    "See NORMSINV"
    return Function("NORM_S_INV", args)


def NORMDIST(*args) -> Function:
    """
    Returns the value of the normal distribution function (or normal cumulative
    distribution function) for a specified value, mean, and standard deviation.
    Learn more: https//support.google.com/docs/answer/3094021
    """
    return Function("NORMDIST", args)


def NORMINV(*args) -> Function:
    """
    Returns the value of the inverse normal distribution function for a specified
    value, mean, and standard deviation.
    Learn more: https//support.google.com/docs/answer/3094022
    """
    return Function("NORMINV", args)


def NORMSDIST(*args) -> Function:
    """
    Returns the value of the standard normal cumulative distribution function for a
    specified value.
    Learn more: https//support.google.com/docs/answer/3094089
    """
    return Function("NORMSDIST", args)


def NORMSINV(*args) -> Function:
    """
    Returns the value of the inverse standard normal distribution function for a
    specified value.
    Learn more: https//support.google.com/docs/answer/3094091
    """
    return Function("NORMSINV", args)


def PEARSON(*args) -> Function:
    """
    Calculates r, the Pearson product-moment correlation coefficient of a dataset.
    Learn more: https//support.google.com/docs/answer/3094092
    """
    return Function("PEARSON", args)


def PERCENTILE(*args) -> Function:
    """
    Returns the value at a given percentile of a dataset.
    Learn more: https//support.google.com/docs/answer/3094093
    """
    return Function("PERCENTILE", args)


def PERCENTILE_EXC(*args) -> Function:
    """
    Returns the value at a given percentile of a dataset, exclusive of 0 and 1.
    Learn more: https//support.google.com/docs/answer/9368167.
    """
    return Function("PERCENTILE_EXC", args)


def PERCENTILE_INC(*args) -> Function:
    "See PERCENTILE"
    return Function("PERCENTILE_INC", args)


def PERCENTRANK(*args) -> Function:
    """
    Returns the percentage rank (percentile) of a specified value in a dataset.
    Learn more: https//support.google.com/docs/answer/3094095
    """
    return Function("PERCENTRANK", args)


def PERCENTRANK_EXC(*args) -> Function:
    """
    Returns the percentage rank (percentile) from 0 to 1 exclusive of a specified
    value in a dataset.
    Learn more: https//support.google.com/docs/answer/3267357
    """
    return Function("PERCENTRANK_EXC", args)


def PERCENTRANK_INC(*args) -> Function:
    """
    Returns the percentage rank (percentile) from 0 to 1 inclusive of a specified
    value in a dataset.
    Learn more: https//support.google.com/docs/answer/3267360
    """
    return Function("PERCENTRANK_INC", args)


def PERMUTATIONA(*args) -> Function:
    """
    Returns the number of permutations for selecting a group of objects (with
    replacement) from a total number of objects.
    Learn more: https//support.google.com/docs/answer/9368324.
    """
    return Function("PERMUTATIONA", args)


def PERMUT(*args) -> Function:
    """
    Returns the number of ways to choose some number of objects from a pool of a
    given size of objects, considering order.
    Learn more: https//support.google.com/docs/answer/3094036
    """
    return Function("PERMUT", args)


def PHI(*args) -> Function:
    """
    The PHI function returns the value of the normal distribution with mean 0 and
    standard deviation 1.
    Learn more: https//support.google.com/docs/answer/9116365.
    """
    return Function("PHI", args)


def POISSON(*args) -> Function:
    "See POISSON.DIST"
    return Function("POISSON", args)


def POISSON_DIST(*args) -> Function:
    """
    Returns the value of the Poisson distribution function (or Poisson cumulative
    distribution function) for a specified value and mean.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/3094097.
    """
    return Function("POISSON_DIST", args)


def PROB(*args) -> Function:
    """
    Given a set of values and corresponding probabilities, calculates the
    probability that a value chosen at random falls between two limits.
    Learn more: https//support.google.com/docs/answer/3094039
    """
    return Function("PROB", args)


def QUARTILE(*args) -> Function:
    """
    Returns a value nearest to a specified quartile of a dataset.
    Learn more: https//support.google.com/docs/answer/3094041
    """
    return Function("QUARTILE", args)


def QUARTILE_EXC(*args) -> Function:
    """
    Returns value nearest to a given quartile of a dataset, exclusive of 0 and 4.
    Learn more: https//support.google.com/docs/answer/9368240.
    """
    return Function("QUARTILE_EXC", args)


def QUARTILE_INC(*args) -> Function:
    "See QUARTILE"
    return Function("QUARTILE_INC", args)


def RANK(*args) -> Function:
    """
    Returns the rank of a specified value in a dataset.
    Learn more: https//support.google.com/docs/answer/3094098
    """
    return Function("RANK", args)


def RANK_AVG(*args) -> Function:
    """
    Returns the rank of a specified value in a dataset. If there is more than one
    entry of the same value in the dataset, the average rank of the entries will be
    returned.
    Learn more: https//support.google.com/docs/answer/3267309
    """
    return Function("RANK_AVG", args)


def RANK_EQ(*args) -> Function:
    """
    Returns the rank of a specified value in a dataset. If there is more than one
    entry of the same value in the dataset, the top rank of the entries will be
    returned.
    Learn more: https//support.google.com/docs/answer/3267310
    """
    return Function("RANK_EQ", args)


def RSQ(*args) -> Function:
    """
    Calculates the square of r, the Pearson product-moment correlation coefficient
    of a dataset.
    Learn more: https//support.google.com/docs/answer/3094099
    """
    return Function("RSQ", args)


def SKEW(*args) -> Function:
    """
    Calculates the skewness of a dataset, which describes the symmetry of that
    dataset about the mean.
    Learn more: https//support.google.com/docs/answer/3094101
    """
    return Function("SKEW", args)


def SKEW_P(*args) -> Function:
    """
    Calculates the skewness of a dataset that represents the entire population.
    Learn more: https//support.google.com/docs/answer/9368569.
    """
    return Function("SKEW_P", args)


def SLOPE(*args) -> Function:
    """
    Calculates the slope of the line resulting from linear regression of a dataset.
    Learn more: https//support.google.com/docs/answer/3094048
    """
    return Function("SLOPE", args)


def SMALL(*args) -> Function:
    """
    Returns the nth smallest element from a data set, where n is user-defined.
    Learn more: https//support.google.com/docs/answer/3094050
    """
    return Function("SMALL", args)


def STANDARDIZE(*args) -> Function:
    """
    Calculates the normalized equivalent of a random variable given mean and
    standard deviation of the distribution.
    Learn more: https//support.google.com/docs/answer/3094102
    """
    return Function("STANDARDIZE", args)


def STDEV(*args) -> Function:
    """
    Calculates the standard deviation based on a sample.
    Learn more: https//support.google.com/docs/answer/3094054
    """
    return Function("STDEV", args)


def STDEV_P(*args) -> Function:
    "See STDEVP"
    return Function("STDEV_P", args)


def STDEV_S(*args) -> Function:
    "See STDEV"
    return Function("STDEV_S", args)


def STDEVA(*args) -> Function:
    """
    Calculates the standard deviation based on a sample, setting text to the value
    `0`.
    Learn more: https//support.google.com/docs/answer/3094055
    """
    return Function("STDEVA", args)


def STDEVP(*args) -> Function:
    """
    Calculates the standard deviation based on an entire population.
    Learn more: https//support.google.com/docs/answer/3094105
    """
    return Function("STDEVP", args)


def STDEVPA(*args) -> Function:
    """
    Calculates the standard deviation based on an entire population, setting text to
    the value `0`.
    Learn more: https//support.google.com/docs/answer/3094058
    """
    return Function("STDEVPA", args)


def STEYX(*args) -> Function:
    """
    Calculates the standard error of the predicted y-value for each x in the
    regression of a dataset.
    Learn more: https//support.google.com/docs/answer/3094108
    """
    return Function("STEYX", args)


def T_DIST(*args) -> Function:
    """
    Returns the right tailed Student distribution for a value x.
    Learn more: https//support.google.com/docs/answer/9369014.
    """
    return Function("T_DIST", args)


def T_DIST_2T(*args) -> Function:
    """
    Returns the two tailed Student distribution for a value x.
    Learn more: https//support.google.com/docs/answer/9368252.
    """
    return Function("T_DIST_2T", args)


def T_DIST_RT(*args) -> Function:
    """
    Returns the right tailed Student distribution for a value x.
    Learn more: https//support.google.com/docs/answer/9369017.
    """
    return Function("T_DIST_RT", args)


def T_INV(*args) -> Function:
    """
    Calculates the negative inverse of the one-tailed TDIST function.
    Learn more: https//support.google.com/docs/answer/6055809
    """
    return Function("T_INV", args)


def T_INV_2T(*args) -> Function:
    """
    Calculates the inverse of the two-tailed TDIST function.
    Learn more: https//support.google.com/docs/answer/6055811
    """
    return Function("T_INV_2T", args)


def T_TEST(*args) -> Function:
    """
    Returns the probability associated with Student's t-test. Determines whether two
    samples are likely to have come from the same two underlying populations that
    have the same mean.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/6055837.
    """
    return Function("T_TEST", args)


def TDIST(*args) -> Function:
    """
    Calculates the probability for Student's t-distribution with a given input (x).
    Learn more: https//support.google.com/docs/answer/3295914
    """
    return Function("TDIST", args)


def TINV(*args) -> Function:
    "See T.INV.2T"
    return Function("TINV", args)


def TRIMMEAN(*args) -> Function:
    """
    Calculates the mean of a dataset excluding some proportion of data from the high
    and low ends of the dataset.
    Learn more: https//support.google.com/docs/answer/3094061
    """
    return Function("TRIMMEAN", args)


def TTEST(*args) -> Function:
    "See T.TEST."
    return Function("TTEST", args)


def VAR(*args) -> Function:
    """
    Calculates the variance based on a sample.
    Learn more: https//support.google.com/docs/answer/3094063
    """
    return Function("VAR", args)


def VAR_P(*args) -> Function:
    "See VARP"
    return Function("VAR_P", args)


def VAR_S(*args) -> Function:
    "See VAR"
    return Function("VAR_S", args)


def VARA(*args) -> Function:
    """
    Calculates an estimate of variance based on a sample, setting text to the value
    `0`.
    Learn more: https//support.google.com/docs/answer/3094064
    """
    return Function("VARA", args)


def VARP(*args) -> Function:
    """
    Calculates the variance based on an entire population.
    Learn more: https//support.google.com/docs/answer/3094113
    """
    return Function("VARP", args)


def VARPA(*args) -> Function:
    """
    Calculates the variance based on an entire population, setting text to the value
    `0`.
    Learn more: https//support.google.com/docs/answer/3094065
    """
    return Function("VARPA", args)


def WEIBULL(*args) -> Function:
    """
    Returns the value of the Weibull distribution function (or Weibull cumulative
    distribution function) for a specified shape and scale.
    Learn more: https//support.google.com/docs/answer/3094116
    """
    return Function("WEIBULL", args)


def WEIBULL_DIST(*args) -> Function:
    "See WEIBULL"
    return Function("WEIBULL_DIST", args)


def Z_TEST(*args) -> Function:
    """
    Returns the one-tailed P-value of a Z-test with standard distribution.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/3094067.
    """
    return Function("Z_TEST", args)


def ZTEST(*args) -> Function:
    "See Z.TEST."
    return Function("ZTEST", args)


def ARABIC(*args) -> Function:
    """
    Computes the value of a Roman numeral.
    Learn more: https//support.google.com/docs/answer/3238301
    """
    return Function("ARABIC", args)


def ASC(*args) -> Function:
    """
    Converts full-width ASCII and katakana characters to their half-width
    counterparts. All standard-width characters will remain unchanged.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9061514
    """
    return Function("ASC", args)


def CHAR(*args) -> Function:
    """
    Convert a number into a character according to the current Unicode table.
    Learn more: https//support.google.com/docs/answer/3094120
    """
    return Function("CHAR", args)


def CLEAN(*args) -> Function:
    """
    Returns the text with the non-printable ASCII characters removed.
    Learn more: https//support.google.com/docs/answer/3267340
    """
    return Function("CLEAN", args)


def CODE(*args) -> Function:
    """
    Returns the numeric Unicode map value of the first character in the string
    provided.
    Learn more: https//support.google.com/docs/answer/3094122
    """
    return Function("CODE", args)


def CONCATENATE(*args) -> Function:
    """
    Appends strings to one another.
    Learn more: https//support.google.com/docs/answer/3094123
    """
    return Function("CONCATENATE", args)


def DOLLAR(*args) -> Function:
    """
    Formats a number into the locale-specific currency format.
    Learn more: https//support.google.com/docs/answer/3094071
    """
    return Function("DOLLAR", args)


def EXACT(*args) -> Function:
    """
    Tests whether two strings are identical.
    Learn more: https//support.google.com/docs/answer/3094073
    """
    return Function("EXACT", args)


def FIND(*args) -> Function:
    """
    Returns the position at which a string is first found within text.
    Learn more: https//support.google.com/docs/answer/3094126
    """
    return Function("FIND", args)


def FINDB(*args) -> Function:
    """
    Returns the position at which a string is first found within text counting each
    double-character as 2.
    Learn more: https//support.google.com/docs/answer/3296009
    """
    return Function("FINDB", args)


def FIXED(*args) -> Function:
    """
    Formats a number with a fixed number of decimal places.
    Learn more: https//support.google.com/docs/answer/3094075
    """
    return Function("FIXED", args)


def JOIN(*args) -> Function:
    """
    Concatenates the elements of one or more one-dimensional arrays using a
    specified delimiter.
    Learn more: https//support.google.com/docs/answer/3094077
    """
    return Function("JOIN", args)


def LEFT(*args) -> Function:
    """
    Returns a substring from the beginning of a specified string.
    Learn more: https//support.google.com/docs/answer/3094079
    """
    return Function("LEFT", args)


def LEFTB(*args) -> Function:
    """
    Returns the left portion of a string up to a certain number of bytes.
    Learn more: https//support.google.com/docs/answer/9367470.
    """
    return Function("LEFTB", args)


def LEN(*args) -> Function:
    """
    Returns the length of a string.
    Learn more: https//support.google.com/docs/answer/3094081
    """
    return Function("LEN", args)


def LENB(*args) -> Function:
    """
    Returns the length of a string in bytes."
    Learn more: https//support.google.com/docs/answer/9367584.
    """
    return Function("LENB", args)


def LOWER(*args) -> Function:
    """
    Converts a specified string to lowercase.
    Learn more: https//support.google.com/docs/answer/3094083
    """
    return Function("LOWER", args)


def MID(*args) -> Function:
    """
    Returns a segment of a string.
    Learn more: https//support.google.com/docs/answer/3094129
    """
    return Function("MID", args)


def MIDB(*args) -> Function:
    """
    Returns a section of a string starting at a given character and up to a
    specified number of bytes.
    Learn more: https//support.google.com/docs/answer/9367691.
    """
    return Function("MIDB", args)


def PROPER(*args) -> Function:
    """
    Capitalizes each word in a specified string.
    Learn more: https//support.google.com/docs/answer/3094133
    """
    return Function("PROPER", args)


def REGEXEXTRACT(*args) -> Function:
    """
    Extracts matching substrings according to a regular expression.
    Learn more: https//support.google.com/docs/answer/3098244
    """
    return Function("REGEXEXTRACT", args)


def REGEXMATCH(*args) -> Function:
    """
    Whether a piece of text matches a regular expression.
    Learn more: https//support.google.com/docs/answer/3098292
    """
    return Function("REGEXMATCH", args)


def REGEXREPLACE(*args) -> Function:
    """
    Replaces part of a text string with a different text string using regular
    expressions.
    Learn more: https//support.google.com/docs/answer/3098245
    """
    return Function("REGEXREPLACE", args)


def REPLACE(*args) -> Function:
    """
    Replaces part of a text string with a different text string.
    Learn more: https//support.google.com/docs/answer/3098247
    """
    return Function("REPLACE", args)


def REPLACEB(*args) -> Function:
    """
    Replaces part of a text string, based on a number of bytes, with a different
    text string.
    Learn more: https//support.google.com/docs/answer/9367752.
    """
    return Function("REPLACEB", args)


def REPT(*args) -> Function:
    """
    Returns specified text repeated a number of times.
    Learn more: https//support.google.com/docs/answer/3094134
    """
    return Function("REPT", args)


def RIGHT(*args) -> Function:
    """
    Returns a substring from the end of a specified string.
    Learn more: https//support.google.com/docs/answer/3094087
    """
    return Function("RIGHT", args)


def RIGHTB(*args) -> Function:
    """
    Returns the right portion of a string up to a certain number of bytes.
    Learn more: https//support.google.com/docs/answer/9367697.
    """
    return Function("RIGHTB", args)


def ROMAN(*args) -> Function:
    """
    Formats a number in Roman numerals.
    Learn more: https//support.google.com/docs/answer/3094153
    """
    return Function("ROMAN", args)


def SEARCH(*args) -> Function:
    """
    Returns the position at which a string is first found within text.
    Learn more: https//support.google.com/docs/answer/3094154
    """
    return Function("SEARCH", args)


def SEARCHB(*args) -> Function:
    """
    Returns the position at which a string is first found within text counting each
    double-character as 2.
    Learn more: https//support.google.com/docs/answer/3295923
    """
    return Function("SEARCHB", args)


def SPLIT(*args) -> Function:
    """
    Divides text around a specified character or string, and puts each fragment into
    a separate cell in the row.
    Learn more: https//support.google.com/docs/answer/3094136
    """
    return Function("SPLIT", args)


def SUBSTITUTE(*args) -> Function:
    """
    Replaces existing text with new text in a string.
    Learn more: https//support.google.com/docs/answer/3094215
    """
    return Function("SUBSTITUTE", args)


def T(*args) -> Function:
    """
    Returns string arguments as text.
    Learn more: https//support.google.com/docs/answer/3094138
    """
    return Function("T", args)


def TEXT(*args) -> Function:
    """
    Converts a number into text according to a specified format.
    Learn more: https//support.google.com/docs/answer/3094139
    """
    return Function("TEXT", args)


def TEXTJOIN(*args) -> Function:
    """
    Combines the text from multiple strings and/or arrays, with a specifiable
    delimiter separating the different texts.
    Learn more: https//support.google.com/docs/answer/7013992
    """
    return Function("TEXTJOIN", args)


def TRIM(*args) -> Function:
    """
    Removes leading and trailing spaces in a specified string.
    Learn more: https//support.google.com/docs/answer/3094140
    """
    return Function("TRIM", args)


def UNICHAR(*args) -> Function:
    """
    Returns the Unicode character for a number.
    Learn more: https//support.google.com/docs/answer/9369024.
    """
    return Function("UNICHAR", args)


def UNICODE(*args) -> Function:
    """
    Returns the decimal Unicode value of the first character of the text.
    Learn more:
    https//support.google.comhttps://support.google.com/docs/answer/9149523
    """
    return Function("UNICODE", args)


def UPPER(*args) -> Function:
    """
    Converts a specified string to uppercase.
    Learn more: https//support.google.com/docs/answer/3094219
    """
    return Function("UPPER", args)


def VALUE(*args) -> Function:
    """
    Converts a string in any of the date, time or number formats that Google Sheets
    understands into a number.
    Learn more: https//support.google.com/docs/answer/3094220
    """
    return Function("VALUE", args)


def DAVERAGE(*args) -> Function:
    """
    Returns the average of a set of values selected from a database table-like array
    or range using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094144
    """
    return Function("DAVERAGE", args)


def DCOUNT(*args) -> Function:
    """
    Counts numeric values selected from a database table-like array or range using a
    SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094222
    """
    return Function("DCOUNT", args)


def DCOUNTA(*args) -> Function:
    """
    Counts values, including text, selected from a database table-like array or
    range using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094147
    """
    return Function("DCOUNTA", args)


def DGET(*args) -> Function:
    """
    Returns a single value from a database table-like array or range using a SQL-
    like query.
    Learn more: https//support.google.com/docs/answer/3094148
    """
    return Function("DGET", args)


def DMAX(*args) -> Function:
    """
    Returns the maximum value selected from a database table-like array or range
    using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094227
    """
    return Function("DMAX", args)


def DMIN(*args) -> Function:
    """
    Returns the minimum value selected from a database table-like array or range
    using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094149
    """
    return Function("DMIN", args)


def DPRODUCT(*args) -> Function:
    """
    Returns the product of values selected from a database table-like array or range
    using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094230
    """
    return Function("DPRODUCT", args)


def DSTDEV(*args) -> Function:
    """
    Returns the standard deviation of a population sample selected from a database
    table-like array or range using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094151
    """
    return Function("DSTDEV", args)


def DSTDEVP(*args) -> Function:
    """
    Returns the standard deviation of an entire population selected from a database
    table-like array or range using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094280
    """
    return Function("DSTDEVP", args)


def DSUM(*args) -> Function:
    """
    Returns the sum of values selected from a database table-like array or range
    using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094281
    """
    return Function("DSUM", args)


def DVAR(*args) -> Function:
    """
    Returns the variance of a population sample selected from a database table-like
    array or range using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094236
    """
    return Function("DVAR", args)


def DVARP(*args) -> Function:
    """
    Returns the variance of an entire population selected from a database table-like
    array or range using a SQL-like query.
    Learn more: https//support.google.com/docs/answer/3094238
    """
    return Function("DVARP", args)


def CONVERT(*args) -> Function:
    """
    Converts a numeric value to a different unit of measure.
    Learn more: https//support.google.com/docs/answer/6055540
    """
    return Function("CONVERT", args)


def TO_DATE(*args) -> Function:
    """
    Converts a provided number to a date.
    Learn more: https//support.google.com/docs/answer/3094239
    """
    return Function("TO_DATE", args)


def TO_DOLLARS(*args) -> Function:
    """
    Converts a provided number to a dollar value.
    Learn more: https//support.google.com/docs/answer/3094241
    """
    return Function("TO_DOLLARS", args)


def TO_PERCENT(*args) -> Function:
    """
    Converts a provided number to a percentage.
    Learn more: https//support.google.com/docs/answer/3094284
    """
    return Function("TO_PERCENT", args)


def TO_PURE_NUMBER(*args) -> Function:
    """
    Converts a provided date/time, percentage, currency or other formatted numeric
    value to a pure number without formatting.
    Learn more: https//support.google.com/docs/answer/3094243
    """
    return Function("TO_PURE_NUMBER", args)


def TO_TEXT(*args) -> Function:
    """
    Converts a provided numeric value to a text value.
    Learn more: https//support.google.com/docs/answer/3094285
    """
    return Function("TO_TEXT", args)


def ARRAY_CONSTRAIN(*args) -> Function:
    """
    Constrains an array result to a specified size.
    Learn more: https//support.google.com/docs/answer/3267036
    """
    return Function("ARRAY_CONSTRAIN", args)


def FREQUENCY(*args) -> Function:
    """
    Calculates the frequency distribution of a one-column array into specified
    classes.
    Learn more: https//support.google.com/docs/answer/3094286
    """
    return Function("FREQUENCY", args)


def GROWTH(*args) -> Function:
    """
    Given partial data about an exponential growth trend, fits an ideal exponential
    growth trend and/or predicts further values.
    Learn more: https//support.google.com/docs/answer/3094287
    """
    return Function("GROWTH", args)


def LINEST(*args) -> Function:
    """
    Given partial data about a linear trend, calculates various parameters about the
    ideal linear trend using the least-squares method.
    Learn more: https//support.google.com/docs/answer/3094249
    """
    return Function("LINEST", args)


def LOGEST(*args) -> Function:
    """
    Given partial data about an exponential growth curve, calculates various
    parameters about the best fit ideal exponential growth curve.
    Learn more: https//support.google.com/docs/answer/3094251
    """
    return Function("LOGEST", args)


def MDETERM(*args) -> Function:
    """
    Returns the matrix determinant of a square matrix specified as an array or
    range.
    Learn more: https//support.google.com/docs/answer/3094290
    """
    return Function("MDETERM", args)


def MINVERSE(*args) -> Function:
    """
    Returns the multiplicative inverse of a square matrix specified as an array or
    range.
    Learn more: https//support.google.com/docs/answer/3094253
    """
    return Function("MINVERSE", args)


def MMULT(*args) -> Function:
    """
    Calculates the matrix product of two matrices specified as arrays or ranges.
    Learn more: https//support.google.com/docs/answer/3094292
    """
    return Function("MMULT", args)


def SUMPRODUCT(*args) -> Function:
    """
    Calculates the sum of the products of corresponding entries in two equal-sized
    arrays or ranges.
    Learn more: https//support.google.com/docs/answer/3094294
    """
    return Function("SUMPRODUCT", args)


def SUMX2MY2(*args) -> Function:
    """
    Calculates the sum of the differences of the squares of values in two arrays.
    Learn more: https//support.google.com/docs/answer/3094257
    """
    return Function("SUMX2MY2", args)


def SUMX2PY2(*args) -> Function:
    """
    Calculates the sum of the sums of the squares of values in two arrays.
    Learn more: https//support.google.com/docs/answer/3094260
    """
    return Function("SUMX2PY2", args)


def SUMXMY2(*args) -> Function:
    """
    Calculates the sum of the squares of differences of values in two arrays.
    Learn more: https//support.google.com/docs/answer/3094298
    """
    return Function("SUMXMY2", args)


def TRANSPOSE(*args) -> Function:
    """
    Transposes the rows and columns of an array or range of cells.
    Learn more: https//support.google.com/docs/answer/3094262
    """
    return Function("TRANSPOSE", args)


def TREND(*args) -> Function:
    """
    Given partial data about a linear trend, fits an ideal linear trend using the
    least squares method and/or predicts further values.
    Learn more: https//support.google.com/docs/answer/3094263
    """
    return Function("TREND", args)


def ENCODEURL(*args) -> Function:
    """
    Encodes a string of text for the purpose of using in a URL query.
    Learn more: https//support.google.com/docs/answer/9199778.
    """
    return Function("ENCODEURL", args)


def HYPERLINK(*args) -> Function:
    """
    Creates a hyperlink inside a cell.
    Learn more: https//support.google.com/docs/answer/3093313
    """
    return Function("HYPERLINK", args)


def IMPORTDATA(*args) -> Function:
    """
    Imports data at a given url in .csv (comma-separated value) or .tsv (tab-
    separated value) format.
    Learn more: https//support.google.com/docs/answer/3093335
    """
    return Function("IMPORTDATA", args)


def IMPORTFEED(*args) -> Function:
    """
    Imports a RSS or ATOM feed.
    Learn more: https//support.google.com/docs/answer/3093337
    """
    return Function("IMPORTFEED", args)


def IMPORTHTML(*args) -> Function:
    """
    Imports data from a table or list within an HTML page.
    Learn more: https//support.google.com/docs/answer/3093339
    """
    return Function("IMPORTHTML", args)


def IMPORTRANGE(*args) -> Function:
    """
    Imports a range of cells from a specified spreadsheet.
    Learn more: https//support.google.com/docs/answer/3093340
    """
    return Function("IMPORTRANGE", args)


def IMPORTXML(*args) -> Function:
    """
    Imports data from any of various structured data types including XML, HTML, CSV,
    TSV, and RSS and ATOM XML feeds.
    Learn more: https//support.google.com/docs/answer/3093342
    """
    return Function("IMPORTXML", args)


def ISURL(*args) -> Function:
    """
    Checks whether a value is a valid URL.
    Learn more: https//support.google.com/docs/answer/3256501
    """
    return Function("ISURL", args)
