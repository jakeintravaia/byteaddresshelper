def main():
  border = ("="*40)
  print(border)
  typeOfCache = input("Direct map or set associative (d/s): ")
  startingPoint = input("Byte address or word address (b/w): ")
  if typeOfCache == "d":
    if startingPoint == "b":
      byteAddress = input("Please enter byte address: ")
    else:
      wordAddress = input("Please enter word address: ")
    blockSize = input("Please enter block size: ")
    cacheSize = input("Please enter amount of blocks in cache: ")
    if startingPoint == "b":
      wordAddress = getWordAddress(byteAddress)
    blockAddress = getBlockAddress(wordAddress, int(blockSize))
    tagIndex = getTagIndex(blockAddress, int(cacheSize))
    print("Word Address: {}".format(wordAddress))
    print("Block Address: {}".format(blockAddress))
    print("Tag | Index: {}".format(tagIndex))
  elif typeOfCache == "s":
    if startingPoint == "b":
      byteAddress = input("Please enter byte address: ")
    else:
      wordAddress = input("Please enter word address: ")
    blockSize = input("Please enter block size: ")
    cacheSize = input("Please enter amount of blocks in cache: ")
    setSize = input("Please enter set size (2 blocks, 4 blocks, etc.): ")
    if startingPoint == "b":
      wordAddress = getWordAddress(byteAddress)
    blockAddress = getBlockAddress(wordAddress, int(blockSize))
    tagSet = getTagSet(blockAddress, int(cacheSize), int(setSize))
    print("Word Address: {}".format(wordAddress))
    print("Block Address: {}".format(blockAddress))
    print("Tag | Set: {}".format(tagSet))
  main()

def getWordAddress(byteAddress):
  size = len(byteAddress)
  return byteAddress[:size - 2]

def getBlockAddress(wordAddress, blockSize):
  size = len(wordAddress)
  removeBits = getPower(blockSize)
  return wordAddress[:size - removeBits]

def getTagIndex(blockAddress, cacheSize):
  size = len(blockAddress)
  removeBits = getPower(cacheSize)
  tag = blockAddress[:size - removeBits]
  index = blockAddress[size - removeBits:]
  return tag + " | " + index

def getTagSet(blockAddress, cacheSize, setSize):
  size = len(blockAddress)
  removeBits = getPower(cacheSize / setSize)
  tag = blockAddress[:size - removeBits]
  set = blockAddress[size - removeBits:]
  return tag + " | " + set

def getPower(n):
  x = 1
  i = 0
  while x != n:
    x *= 2
    i += 1
    if x > n:
      print("ERROR: Number entered is not a power of two.")
      break
  return i


if __name__ == "__main__":
  main()
