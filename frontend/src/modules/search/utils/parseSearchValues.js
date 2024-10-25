export const parseSearchValues = (values) => {
  const { text, fileMask, size, creationTime } = values

  return {
    text,
    fileMask,
    size: size?.value ? size : undefined,
    creationTime: creationTime?.value ? {...creationTime, value: creationTime.value.toISOString()} : undefined,
  }
}