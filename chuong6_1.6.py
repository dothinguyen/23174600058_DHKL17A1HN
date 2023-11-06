alice_candies = 121
bob_candies = 77
carol_candies = 109

total_candies = alice_candies + bob_candies + carol_candies
candies_per_person = 30

leftover_candies = total_candies % candies_per_person

print("Số kẹo dư sau khi chia đều cho Alice, Bob và Carol là:", leftover_candies)
