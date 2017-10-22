if __name__ == "__main__":
  tickets_cnt = int(raw_input())
  tickets_i = 0
  tickets = []
  while tickets_i < tickets_cnt:
    tickets_item = int(raw_input());
    tickets.append(tickets_item)
    tickets_i += 1
  p = int(raw_input());
  print(tickets)
