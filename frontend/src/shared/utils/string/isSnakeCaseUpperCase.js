export const isSnakeCaseUpperCase = (key) => {
  const pattern = /^[A-Z0-9_]+$/
  return pattern.test(key)
}
