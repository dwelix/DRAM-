score = 0
totalscore1 = 0
print(" .・。.・゜✭・ Welcome to the DRAM Mental Health Questionaire!! .・✫・゜・。.")
print("\nplease answer these questions honestly to get an accurate answer ~ thank you ~ ")
print("Type a letter and not the whole word, for example, a, b, c, d")

def get_valid_response(valid_responses):
    while True:
        response = input('Enter the answer: ').strip().upper()
        if response in valid_responses:
            return response
        else:
            print('Please enter a valid response. The value should be A,B,C or D')

#Question1
print('\n1. When you experience conflicts or misunderstandings with someone in your social circle, how does it impact your emotions?')
print(' a) Upset')
print(' b) Unaffected')
print(' c) Motivated to resolve')
print(' d) Resigned')
response1 = get_valid_response(['A', 'B', 'C', 'D'])

if response1 == 'A':
    score = 2
    totalscore1 = totalscore1 + score
elif response1 == 'B':
    score = 3
    totalscore1 = totalscore1 + score
elif response1 == 'C':
    score = 1
    totalscore1 = totalscore1 + score
elif response1 == 'D':
    score = 4
    totalscore1 += score

# Question2
print('\n2. How do you emotionally assess the quality of your social relationships?')
print(' a) Positively; emotional depth and support matter most')
print(' b) Anxiously; I often gauge it by the size of my social circle')
print(' c) Balanced; I consider both depth and breadth of connections')
print(' d) Indifferently; I don\'t think about social relationships much')
response2 = get_valid_response(['A', 'B', 'C', 'D'])

if response2 == 'A':
    score = 3
    totalscore1 = totalscore1 + score
elif response2 == 'B':
    score = 2
    totalscore1 = totalscore1 + score
elif response2 == 'C':
    score = 4
    totalscore1 = totalscore1 + score
elif response2 == 'D':
    score = 1
    totalscore1 = totalscore1 + score

#Question3
print('\n3. How do you feel when you have the opportunity to help or support a friend or family member in need?')
print(' a) Fulfilled ')
print(' b) Happy')
print(' c) Stressed')
print(' d) Guilty')
response3 = get_valid_response(['A', 'B', 'C', 'D'])
if response3 == 'A':
    score = 4
    totalscore1 = totalscore1 + score
elif response3 == 'B':
    score = 3
    totalscore1 = totalscore1 + score
elif response3 == 'C':
    score = 2
    totalscore1 = totalscore1 + score
elif response3 == 'D':
    score = 1
    totalscore1 = totalscore1 + score

#Question4
print('\n4. What does a socially fulfilling life mean to you?')
print(' a) Attending numerous parties and events')
print(' b) Building deep, meaningful relationships')
print(' c) Receiving social media likes and comments')
print(' d) Pursuing individual interests without external influences')
response4 = get_valid_response(['A', 'B', 'C', 'D'])
if response4 == 'A':
    score = 4
    totalscore1 = totalscore1 + score
elif response4 == 'B':
    score = 3
    totalscore1 = totalscore1 + score
elif response4 == 'C':
    score = 2
    totalscore1 = totalscore1 + score
elif response4 == 'D':
    score = 1
    totalscore1 = totalscore1 + score    
    

score2 = 0
totalscore2 = 0

#Question5
print('\n5. How does spending quality time with loved ones make you feel?')
print(' a) Really happy')
print(' b) Happy')
print(' c) Sad')
print(' d) Really sad')
response5 = get_valid_response(['A', 'B', 'C', 'D'])
if response5 == 'A':
    score2 = 4
    totalscore2 = totalscore2 + score
elif response5 == 'B':
    score2 = 3
    totalscore2 = totalscore2 + score
elif response5 == 'C':
    score2 = 2
    totalscore2 = totalscore2 + score
elif response5 == 'D':
    score2 = 1
    totalscore2 = totalscore2 + score

#Question6
print('\n6. What emotions do you experience when you accomplish something youve worked hard for?')
print(' a) Proud and elated')
print(' b) Content')
print(' c) Indifferent')
print(' d) Disappointed')
response6 = get_valid_response(['A', 'B', 'C', 'D'])
if response6 == 'A':
    score2 = 4
    totalscore2 = totalscore2 + score
elif response6 == 'B':
    score2 = 3
    totalscore2 = totalscore2 + score
elif response6 == 'C':
    score2 = 1
    totalscore2 = totalscore2 + score
elif response6 == 'D':
    score2 = 2
    totalscore2 = totalscore2 + score 
    
#Question7
print('\n7. How does receiving praise or recognition for your achievements affect your emotions?')
print(' a) Extremely pleased and appreciated')
print(' b) Happy')
print(' c) Neutral')
print(' d) Anxious or uncomfortable')
response7 = get_valid_response(['A', 'B', 'C', 'D'])
if response7 == 'A':
    score2 = 4
    totalscore2 = totalscore2 + score
elif response7 == 'B':
    score2 = 3
    totalscore2 = totalscore2 + score
elif response7 == 'C':
    score2 = 2
    totalscore2 = totalscore2 + score
elif response7 == 'D':
    score2 = 1
    totalscore2 = totalscore2 + score 
    
#Question8
print('\n8. What emotions arise when you engage in activities that youre passionate about?')
print(' a) Exhilarated')
print(' b) Joyful')
print(' c) Bored')
print(' d) Frustrated')
response8 = get_valid_response(['A', 'B', 'C', 'D'])
if response8 == 'A':
    score2 = 4
    totalscore2 = totalscore2 + score
elif response8 == 'B':
    score2 = 3
    totalscore2 = totalscore2 + score
elif response8 == 'C':
    score2 = 2
    totalscore2 = totalscore2 + score
elif response8 == 'D':
    score2 = 1
    totalscore2 = totalscore2 + score     
    

score3 = 0
totalscore3 = 0

#Question9
print('\n9. How does successfully solving a challenging problem or puzzle make you feel?')

print(' a) Really happy and accomplished')
print(' b) Happy')
print(' c) Neutral')
print(' d) Anxious')
response9 = get_valid_response(['A', 'B', 'C', 'D'])
if response9 == 'A':
    score3 = 4
    totalscore3 = totalscore3 + score
elif response9 == 'B':
    score3 = 3
    totalscore3 = totalscore3 + score
elif response9 == 'C':
    score3 = 2
    totalscore3 = totalscore3 + score
elif response9 == 'D':
    score3 = 1
    totalscore = totalscore3 + score 
    
#Question10
print('\n10. What emotions do you experience when you learn something new or gain a deeper understanding of a topic youre interested in?')
print(' a) Excited and intellectually fulfilled')
print(' b) Satisfied')
print(' c) Uninterested')
print(' d) Overwhelmed')
response10 = get_valid_response(['A', 'B', 'C', 'D'])
if response10 == 'A':
    score3 = 4
    totalscore3 = totalscore3 + score
elif response10 == 'B':
    score3 = 3
    totalscore3 = totalscore3 + score
elif response10 == 'C':
    score3 = 1
    totalscore3 = totalscore3 + score
elif response10 == 'D':
    score3 = 2
    totalscore3 = totalscore3 + score 
    
#Question11
print('\n11. How does your ability to concentrate and focus on tasks impact your emotions and overall well-being?')
print(' a) Clear-minded and focused')
print(' b) Content')
print(' c) Distracted')
print(' d) Stressed')
response11 = get_valid_response(['A', 'B', 'C', 'D'])
if response11 == 'A':
    score3 = 4
    totalscore3 = totalscore3 + score
elif response11 == 'B':
    score3 = 3
    totalscore3 = totalscore3 + score
elif response11 == 'C':
    score3 = 1
    totalscore3 = totalscore3 + score
elif response11 == 'D':
    score3 = 2
    totalscore3 = totalscore3 + score 
    
#Question12
print('\n12. What emotions do you associate with moments of creative inspiration or when you engage in creative activities?')
print(' a) Inspired and creative')
print(' b) Fulfilled')
print(' c) Neutral')
print(' d) Blocked or uncreative')
response12 = get_valid_response(['A', 'B', 'C', 'D'])
if response12 == 'A':
    score3 = 4
    totalscore3 = totalscore3 + score
elif response12 == 'B':
    score3 = 3
    totalscore3 = totalscore3 + score
elif response12 == 'C':
    score3 = 2
    totalscore3 = totalscore3 + score
elif response12 == 'D':
    score3 = 1
    totalscore3 = totalscore3 + score 


score4 = 0
totalscore4 = 0


#Question13
print('\n13. How does your emotional state relate to the importance of a healthy lifestyle for physical well-being?')
print(' a) Positive; a balanced diet and exercise emotionally uplift me')
print(' b) Stressful; I feel pressured to follow health trends, causing emotional strain')
print(' c) Challenging; striving for a specific body shape can be emotionally demanding')
print(' d) Emotionally neutral; physical health doesnt significantly impact my emotions')
response13 = get_valid_response(['A', 'B', 'C', 'D'])
if response13 == 'A':
    score4 = 4
    totalscore4 = totalscore4 + score
elif response13 == 'B':
    score4 = 1
    totalscore4 = totalscore4 + score
elif response13 == 'C':
    score4 = 2
    totalscore4 = totalscore4 + score
elif response13 == 'D':
    score4 = 3
    totalscore4 = totalscore4 + score 
    
#Question14
print('\n14. How do your emotions connect with the importance of rest and relaxation for physical well-being?')
print(' a) Comforting; rest and relaxation emotionally recharge me')
print(' b) Frustrating; I often neglect rest due to a busy schedule, leading to emotional unrest')
print(' c) Emotionally situational; I rest when Im exceptionally fatigued')
print(' d) Emotionally indifferent; rest doesnt strongly affect my emotions')
response14 = get_valid_response(['A', 'B', 'C', 'D'])
if response14 == 'A':
    score4 = 4
    totalscore4 = totalscore4 + score
elif response14 == 'B':
    score4 = 1
    totalscore4 = totalscore4 + score
elif response14 == 'C':
    score4 = 2
    totalscore4 = totalscore4 + score
elif response14 == 'D':
    score4 = 3
    totalscore4 = totalscore4 + score
    
#Question15
print('\n15. How does being in a clean and organised physical environment impact your emotional state?')
print(' a) Content and at ease')
print(' b) Neutral')
print(' c) Anxious or stressed')
print(' d) Overwhelmed')
response15 = get_valid_response(['A', 'B', 'C', 'D'])
if response15 == 'A':
    score4 = 4
    totalscore4 = totalscore4 + score
elif response15 == 'B':
    score4 = 3
    totalscore4 = totalscore4 + score
elif response15 == 'C':
    score4 = 2
    totalscore4 = totalscore4 + score
elif response15 == 'D':
    score4 = 1
    totalscore4 = totalscore4 + score
    
#Question16
print('\n16. What emotions are associated with maintaining good personal hygiene and grooming habits?')
print(' a) Fresh and confident')
print(' b) Satisfied')
print(' c) Unkempt or uncomfortable')
print(' d) Indifferent')
response16 = get_valid_response(['A', 'B', 'C', 'D'])
if response16 == 'A':
    score4 = 4
    totalscore4 = totalscore4 + score
elif response16 == 'B':
    score4 = 3
    totalscore4 = totalscore4 + score
elif response16 == 'C':
    score4 = 2
    totalscore4 = totalscore4 + score
elif response16 == 'D':
    score4 = 1
    totalscore4 = totalscore4 + score
    

if totalscore1 + totalscore2 + totalscore3 + totalscore4 >= 16 and totalscore1 + totalscore2 + totalscore3 + totalscore4 < 25:
    print("\nYour overall well-being is in a challenging state, indicating multiple areas of concern.\n\nSuggestions:\nSeek professional help or counseling to address various well-being issues. \nPrioritize self-care practices and emotional support. \nWork on conflict resolution, emotional management, and stress reduction \nHere are some resources and services related to social well-being that are available in Asia: \nMental Health Asia : https://www.mentalhealthasia.org/ \nBefrienders Worldwide: https://www.befrienders.org \n" )
elif totalscore1 + totalscore2 + totalscore3 + totalscore4 >= 25 and totalscore1 + totalscore2 + totalscore3 + totalscore4 < 40:
    print("\nYour overall well-being needs significant improvement, as multiple aspects of your life are affected.\n\nSuggestions: \nSeek support from a mental health professional to address specific concerns. \nFocus on self-care, stress management, and building healthier relationships. Set achievable goals for well-being enhancement. \nHere are some resources and services related to social well-being that are available in Asia: \nMental Health Asia : https://www.mentalhealthasia.org/ \nBefrienders Worldwide: https://www.befrienders.org \n")
elif totalscore1 + totalscore2 + totalscore3 + totalscore4 >= 41 and totalscore1 + totalscore2 + totalscore3 + totalscore4 < 56:
    print("\nYour overall well-being is at an average level, indicating a mix of strengths and areas for improvement.\n\nSuggestions: \nMaintain good mental health habits and well-being practices. \nWork on specific aspects of life, such as relationships and emotional management. \nExplore new hobbies and interests for added fulfillment. \nHere are some resources and services related to social well-being that are available in Asia: \nMental Health Asia : https://www.mentalhealthasia.org/ \nBefrienders Worldwide: https://www.befrienders.org \n")
else:
    print("\nCongratulations! Your overall well-being is in a positive and stable state.\n\nSuggestions:\nContinue your excellent well-being practices to sustain and enhance your quality of life. \nShare your experiences and insights with others to inspire and support their well-being journeys. \nConsider helping and supporting those who may be struggling with their well-being, as you have valuable knowledge and experience to share \nHere are some resources and services related to social well-being that are available in Asia: \nMental Health Asia : https://www.mentalhealthasia.org/ \nBefrienders Worldwide: https://www.befrienders.org \n")

if totalscore1 > 0 and totalscore1 < 9:
    print("\nYou tend to feel very upset or resigned when conflicts arise, indicating challenges in managing social conflicts.Consider developing better conflict resolution skills."
"You may rely heavily on the size of your social circle to assess the quality of your relationships. Consider focusing on the depth and emotional support within your relationships." 
"You may often feel stressed or guilty when helping others, suggesting a need to manage your emotional responses to caregiving."
"If you value attending numerous parties and events for social fulfilment, you may benefit from exploring deeper, more meaningful connections.")
elif totalscore1 > 8 and totalscore1 < 17:
    print("\nYou generally respond to conflicts with a mix of emotions, which is a common reaction. Continue working on your conflict resolution skills to maintain better social well-being."
"Your balanced approach to assessing relationships is healthy. Continue nurturing both the depth and breadth of your connections for improved social well-being."	
"Feeling fulfilled or happy when helping others is a positive sign of social well-being. Continue being supportive and nurturing in your relationships."
"Prioritising deep and meaningful relationships is a sign of strong social well-being. Keep nurturing these connections for a fulfilling social life.")

if totalscore2 > 0 and totalscore2 < 9:
    print("\nFeeling sad or really sad when spending time with loved ones may indicate emotional challenges in your relationships. Seek support to address these emotions."
"Feeling indifferent or disappointed after accomplishing hard work suggests room for improvement in recognising and celebrating your achievements."
"Feeling anxious or uncomfortable when praised may indicate a need to work on accepting compliments and recognition gracefully."
"Feeling bored or frustrated during activities you're passionate about suggests room for finding more engaging and fulfilling pursuits.")

if totalscore2 > 8 and totalscore2 < 17: 
    print("\nFeeling really happy or happy when with loved ones is a positive sign of emotional well-being. Continue cherishing these moments."
"Feeling proud and elated or content after hard work is a positive indicator of emotional well-being. Continue acknowledging and celebrating your accomplishments."
"Feeling extremely pleased and appreciated or happy when recognised is a sign of emotional well-being. Embrace these positive emotions."
"Feeling exhilarated or joyful during passionate activities is a sign of emotional well-being. Continue pursuing your passions for emotional fulfilment.")

if totalscore3 > 0 and totalscore3 < 9:
    print("\n Feeling anxious after solving challenging problems may indicate a need to build confidence in your problem-solving abilities."
"Feeling uninterested or overwhelmed when learning something new suggests a need to find topics that genuinely engage your curiosity."
"Feeling distracted or stressed due to poor focus may indicate the need to develop better concentration strategies."
"Feeling blocked or uncreative during creative moments suggests a need to explore new sources of inspiration.")

if totalscore3 > 8 and totalscore3 < 17:
    print("\n Feeling really happy and accomplished or happy after solving challenges is a positive sign of cognitive well-being. Trust your problem-solving skills."
"Feeling excited and intellectually fulfilled or satisfied when learning is a sign of cognitive well-being. Keep exploring your interests."
"Feeling clear-minded and focused or content while concentrating is a positive sign of cognitive well-being. Maintain focus on tasks."
"Feeling inspired and creative or fulfilled during creative activities is a sign of cognitive well-being. Embrace your creativity.")

if totalscore4 > 0 and totalscore4 < 9:
    print("\n Feeling stressed or pressured by health trends indicates emotional strain related to physical well-being. Focus on balanced, sustainable choices."
"Neglecting rest and feeling emotionally unrestful suggests the need to prioritise self-care and relaxation for overall well-being."
"Feeling anxious or stressed in an unorganised environment suggests the need for decluttering and maintaining order for emotional well-being."
"Feeling unkempt or uncomfortable due to poor personal hygiene may indicate the need for improved grooming habits for emotional well-being.")

if totalscore4 > 8 and totalscore4 < 17:
    print("\nFeeling positive and uplifted by a balanced diet and exercise is a sign of emotional alignment with physical well-being. Maintain healthy habits."
"Finding emotional comfort and recharging through rest and relaxation indicates emotional alignment with physical well-being. Prioritise self-care."
"Feeling content and at ease in a clean and organised space is a positive indicator of emotional alignment with physical well-being. Maintain a tidy environment."
"Feeling fresh and confident with good personal hygiene and grooming is a sign of emotional alignment with physical well-being. Maintain good hygiene habits.")
