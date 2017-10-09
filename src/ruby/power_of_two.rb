def is_power_of_two(n)
  return true if n == 1
  return false if n == 0
  while n % 2 == 0
    n /= 2
    return true if n == 1
  end
  return false
end