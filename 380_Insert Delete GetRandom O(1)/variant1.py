# Create a lottery storage system that would allow you to add,
# remove and pick participants. This storage system must run
# at O(1) and participants must be picked at random.

# Functions to implement:
#   void LotterySystem() - Create Lottery object
#   boolean addParticipant(int id) - Add a participant (Unique id)
#                                    return true when successfully added
#                                    return false if they cannot
#                                    be added
#   boolean removeParticipant(int id) - Remove a participant (Unique id)
#                                    return true when successfully removed
#                                    return false if they could not
#                                    be removed
#   int randomPick() - Randomly select a lottery winner and return
#                      their ID.
#                      Return -1 if there are no participants left.        

# https://leetcode.com/discuss/post/6607794/bloomberg-intern-swe-london-offered-by-k-jnlw/