scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

index = 0
total_tests = len(scores)

while (index < total_tests):
    score = scores[index]
    print("Bubble solution #" + str(index), "score: ", score)
    index = index+1

#the number of records in the list
print("Bubbles tests: ", total_tests) 

#the highest score in the list

print("Highest bubble score: ", max(scores))
#the solutions that contain the highest score, e.g. [11, 18]

max_score = max(scores) #69
max_scores = [] #[11, 18]

for i, score in enumerate(scores):
    if score == max_score:
        # append to max_scores the index value of score
        max_scores.append(i)


print("Solutions with highest score:", max_scores) # [11, 18]


#using the score list
#for as long as there are addresses
#open the first index
#see if its value equals max address
#if so, insert the index address to an array
#move on to next index value until all 
    

