export const makeString = (separator, ...args) =>
  args
    .filter((value) => Boolean(value))
    .map((str) => str.trim())
    .join(separator)
