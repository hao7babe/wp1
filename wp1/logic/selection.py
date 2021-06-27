import urllib.parse


def validate_list(items):
  item_list = items.split("\n")
  invalid_article_names = []
  valid_article_names = []
  for item in item_list:
    item_in_invalid_article_names = False
    item = item.strip().replace(" ", "_")
    decoded_item = urllib.parse.unquote(item)
    len_item = len(decoded_item.encode("utf-8"))
    sets = {"#", "<", ">", "[", "]", "{", "}", "|"}
    if len_item > 256:
      invalid_article_names.append(decoded_item)
      item_in_invalid_article_names = True
      continue
    for forbiden_character in sets:
      if forbiden_character in decoded_item:
        invalid_article_names.append(decoded_item)
        item_in_invalid_article_names = True
        break
    if not item_in_invalid_article_names:
      article_name = decoded_item.replace(
          "https://en.wikipedia.org/wiki/",
          "").replace("https://en.wikipedia.org/w/index.php?title=", "")
      valid_article_names.append(article_name)
  return (valid_article_names, invalid_article_names)
