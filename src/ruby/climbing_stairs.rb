def climb_stairs(n)
  return n if n < 4
  pairs = n / 2
  steps = 0
  for p in 0..pairs
    remainder = n - (2 * p)
    # Ruby doesn't have a factorial function: I used inject method.
    divider2 = (1..p).reduce(:*) || 1
    divider1 = (1..remainder).reduce(:*) || 1
    dividend = (1..(remainder + p)).reduce(:*) || 1
    steps += dividend / (divider1 * divider2)
  end
  steps
end