def max_profit(prices)
  return 0 if prices.length < 2
  descending = true
  for i in 1...prices.length
    current = prices[(i-1)]
    next_val = prices[i]
    descending = false if current < next_val
  end
  return 0 if descending

  profit = 0
  last_idx = prices.length - 1
  for idx in 0...(last_idx)
    to_buy = prices[idx]
    possibile_days = prices.drop(idx+1)
    to_sell = possibile_days.max
    if to_sell > to_buy
      deal = to_sell - prices[idx]
      profit = deal if deal > profit
    end
  end
  profit
end

def max_profit2(prices)
  return 0 if prices.length < 2

  min_price = prices[0]
  max_profit = 0
  prices.each do |price|
    profit = price - min_price

    if price < min_price
      min_price = price
    elsif profit > max_profit
      max_profit = profit
    end
  end
  max_profit
end
