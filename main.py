import streamlit as st

# Display image
st.image("Apps Logo.PNG")

import streamlit as st

class BrainBasedCareerAdvisor:
    def __init__(self):
        self.questions = [
            "1) Do you prefer a) working with numbers or b) creating art?",
            "2) What are your favorite activities, a) like solving puzzles or b) drawing?",
            "3) Do you enjoy a) reading or b) watching movie?",
            "4) Do you like to a) follow instructions or b) create your own way of doing things?",
            "5)Do you enjoy a) logic games or b) creative storytelling?",
            "6) Do you prefer a) detailed tasks or b) big-picture ideas?",
            "7) Do you like to work in a) an organized environment or b) a more flexible one?",
            "8) Do you follow a) a schedule or b) do things spontaneously?",
            "9) Do you prefer a) structured learning or b) hands-on projects?",
            "10) Do you enjoy a)critical thinking or b) imaginative thinking more?"
        ]
        self.career_suggestions = {
            'left_brained': ['Engineer', 'Accountant', 'Data Analyst','Financial Analyst','Software Developer','Doctor','Lawyer','Architect','Economist','Programmer'],
            'right_brained': ['Multimedia Animator', 'Writer', 'Fashion Designer','Interior Designer', 'Musician','Photographer','Journalist','Dancer','Actor','Writer'],
            'balanced': ['Educator/Teacher', 'Entrepreneur', 'IT Manager', 'UI/UX Designer,''Marketing Manager','Business Analyst','Researcher','Data Scientist','Project Manager','Lecturer']
        }
        

    def determine_brain_dominance(self, answers):
        left_brain_count = sum(1 for answer in answers if answer == 'A')
        right_brain_count = sum(1 for answer in answers if answer == 'B')

        if left_brain_count > right_brain_count:
            return 'left_brained'
        elif right_brain_count > left_brain_count:
            return 'right_brained'
        else:
            return 'balanced'

    def suggest_careers(self, dominance):
        careers = self.career_suggestions[dominance]
        return careers

advisor = BrainBasedCareerAdvisor()

def main():
    #st.title("Brain-Based Career Advisor")
    st.markdown(f"<br>", unsafe_allow_html=True)
    st.write("Welcome to Brain-based Career Advisor. I will ask you 10 questions to determine your brain dominance and suggest suitable careers for you.")

    answers = []
    for i, question in enumerate(advisor.questions):
        st.markdown(f"<h6>{question}</h6>", unsafe_allow_html=True)
        answer = st.radio("", ('A', 'B'), key=i)
        answers.append(answer)
        st.markdown(f"<br>", unsafe_allow_html=True)

    if st.button("Submit"):
        dominance = advisor.determine_brain_dominance(answers)
        st.write ('<br>', unsafe_allow_html=True)
        st.write(f"Based on your answers, your brain dominance is {dominance.replace('_', ' ')}.")
        
        careers = advisor.suggest_careers(dominance)
        st.write ('<br>', unsafe_allow_html=True)
        st.write('<b>Here are some career options for you:</b>', unsafe_allow_html=True)
        
        for career in careers:
            st.write(career)

    
        st.write ('<br><br><b>Left-brain dominance</b> is often associated with characteristics related to logical, analytical, and detail-oriented thinking.<br>', unsafe_allow_html=True)

        st.write ('<b>Right-brain dominance</b> is generally associated with traits related to creativity, intuition, and holistic thinking.<br>', unsafe_allow_html=True)
          
        st.write ('<b>Balanced-brain dominance</b> refers to a cognitive style where an individual effectively integrates both left-brain and right-brain characteristics. This balance allows for a versatile approach to thinking and problem-solving.<br>', unsafe_allow_html=True)
          
        st.write ('<b>Besides the suggested career, you can explore other related careers that you think are suitable for your future based on your brain-hemisphere dominance characteristics.</b>', unsafe_allow_html=True)
       

# Disclaimer
        st.write('<br><br><b>Disclaimer</b>: The information and recommendations provided by this brain-based career advisor app are intended for general guidance and informational purposes only and should not be construed as professional career advice. While the app utilizes advanced algorithms and cognitive science principles to offer career insights, it does not guarantee specific outcomes or results. Users should consult with qualified career professionals or advisors before making any significant career decisions. The developers of this app expressly disclaim any liability for any actions taken or not taken based on the information provided, and users assume all risks associated with their use of the app.', unsafe_allow_html=True)

    

if __name__ == '__main__':
    main()