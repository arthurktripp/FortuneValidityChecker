from flask import Flask, request, render_template
import json
import re

app = Flask(__name__)


letters = 0
letters_ans = ""
letters_punct = 0
letters_punct_ans = ""               

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        global letters, letters_ans, letters_punct, letters_punct_ans
        letters = 0
        letters_ans = ""
        letters_punct = 0
        letters_punct_ans = "" 
        
        data = request.form
        fortune, nums = create_num_list(data)
        fortunate(nums, fortune)
        
        if letters_ans == "":
            letters_ans = "Your numbers don't add up."
        if letters_punct_ans == "":
            letters_punct_ans = "Your numbers don't add up."
        
        return render_template('answer.html',
                               fortune = fortune,
                               nums = nums,
                               letters = letters,
                               letters_ans = letters_ans,
                               letters_punct = letters_punct,
                               letters_punct_ans = letters_punct_ans)



def create_num_list(data):
    nums = []
    for key, val in data.items():
        if key == 'fortune':
            continue
        try:
            val = int(val)
            nums.append(val)
        except:
            continue
    return data['fortune'], nums



def fortunate(nums, a_string):
    punc_regex = r'[\W_]'
    no_punc = re.sub(punc_regex, '', a_string)
    fortunate_numbers1(nums, no_punc)
    fortunate_numbers2(nums, a_string)
    global letters, letters_punct
    letters = len(no_punc)
    letters_punct = len(a_string)


def fortunate_numbers1(nums: list, fortune: str, answer="", total=0):
    if total == len(fortune):
        global letters_ans
        letters_ans = answer
        return True
    while nums:
        if fortunate_numbers1(nums[1:], fortune, answer + "+" + str(nums[0]), total + nums[0]):
            return True
        elif fortunate_numbers1(nums[1:], fortune, answer + "-" + str(nums[0]), total - nums[0]):
            return True
        elif fortunate_numbers1(nums[1:], fortune, answer, total):
            return True
        return False


def fortunate_numbers2(nums: list, fortune: str, answer="", total=0):
    if total == len(fortune):
        global letters_punct_ans
        letters_punct_ans = answer
        return True
    while nums:
        if fortunate_numbers2(nums[1:], fortune, answer + "+" + str(nums[0]), total + nums[0]):
            return True
        elif fortunate_numbers2(nums[1:], fortune, answer + "-" + str(nums[0]), total - nums[0]):
            return True
        elif fortunate_numbers2(nums[1:], fortune, answer, total):
            return True
        return False




if __name__ == "__main__":
  app.run(port=5002, debug = True)