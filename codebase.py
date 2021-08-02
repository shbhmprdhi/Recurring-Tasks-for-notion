if(
  dateBetween(
    now(),
    prop("Due"),
    "days"
  ) >= 1 and unequal(
    formatDate(
      now(), "L"
    ),
    formatDate(
      prop("Due"), "L"
    )
  ) and unequal(
    prop("Type"),
    "One-Time"
  ),
  if(
    equal(
      dateBetween(
        now(),
        prop("Due"),
        "days"
      ) /
      prop("Recur Interval (Days)"),
      ceil(
        dateBetween(
          now(),
          prop("Due"),
          "days"
        ) /
        prop("Recur Interval (Days)")
      )
    ),
    dateAdd(
      prop("Due"),
      multiply(
        dateBetween(
          now(),
          prop("Due"),
          "days"
        ) /
        prop("Recur Interval (Days)") + 1,
        prop("Recur Interval (Days)")
      ),
      "days"
    ),
    dateAdd(
      prop("Due"),
      multiply(
        ceil(
          dateBetween(
            now(),
            prop("Due"),
            "days"
          ) /
          prop("Recur Interval (Days)")
        ),
        prop("Recur Interval (Days)")
      ),
      "days"
    )
  ),
  dateAdd(
    prop("Due"),
    prop("Recur Interval (Days)"),
    "days"
  )
)
