from django.template import Library
from django.utils.translation import gettext as _, ngettext

from dateutil.relativedelta import relativedelta

register = Library()


@register.filter
def duration(rel_delta: relativedelta) -> str:
    bits = []

    if rel_delta.years:
        bits.append(
            ngettext("{years} year", "{years} years", rel_delta.years,).format(
                years=rel_delta.years
            )
        )

    if rel_delta.months:
        bits.append(
            ngettext("{months} month", "{months} months", rel_delta.months,).format(
                months=rel_delta.months
            )
        )

    if rel_delta.days:
        bits.append(
            ngettext("{days} day", "{days} days", rel_delta.days,).format(
                days=rel_delta.days
            )
        )

    if rel_delta.hours:
        bits.append(
            ngettext("{hours} hour", "{hours} hours", rel_delta.hours,).format(
                hours=rel_delta.hours
            )
        )

    if rel_delta.minutes:
        bits.append(
            ngettext(
                "{minutes} minute", "{minutes} minutes", rel_delta.minutes,
            ).format(minutes=rel_delta.minutes)
        )

    if rel_delta.seconds:
        bits.append(
            ngettext(
                "{seconds} second", "{seconds} seconds", rel_delta.seconds,
            ).format(seconds=rel_delta.seconds)
        )

    if not bits:
        return "-"

    if len(bits) == 1:
        return bits[0]

    last = bits[-1]
    first = ", ".join(bits[:-1])
    return _("{first} and {last}").format(first=first, last=last)
