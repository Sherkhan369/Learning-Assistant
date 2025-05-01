import streamlit as st
from recommender import Recommender


def run_gui():
    recommender = Recommender()
    today_info = recommender.get_today_topic()

    st.title("🧠 Daily Learning Assistant")

    # Search Section
    st.subheader("🔍 Enter your topic:")
    search_query = st.text_input("Topic name:", key="search_input")

    if st.button("Search", key="search_button"):
        if search_query:
            result = recommender.get_topic_info(search_query)
            if result:
                st.subheader(f"🔎 Result for '{search_query}':")
                st.code(result["code"], language="python")
                st.write(f"📅 Topic: {result['topic']}")

                # YouTube Link Display
                if "youtube" in result and result["youtube"].startswith("http"):
                    st.markdown(f"🔗 [Watch Recommended YouTube Video]({result['youtube']})", unsafe_allow_html=True)
                else:
                    st.write(f"🔗 YouTube: {result['youtube']}")
            else:
                st.warning("❗ Topic not found.")


    # Today's Topic Display
    if today_info:
        st.subheader(f"📅 Today's Topic: {today_info['topic']}")
        st.code(today_info["code"], language="python")

        if "youtube" in today_info and today_info["youtube"].startswith("http"):
            st.markdown(f"🔗 [Watch Recommended YouTube Video]({today_info['youtube']})", unsafe_allow_html=True)
        else:
            st.write(f"🔗 YouTube: {today_info['youtube']}")

    # Quiz Section
    if today_info:
        quizzes = recommender.get_quiz(today_info["topic"])
    if quizzes:
        for i, quiz in enumerate(quizzes):
            st.write(f"**Question {i+1}:** {quiz['question']}")
            selected = st.radio(f"Select your answer:", quiz["options"], key=f"quiz_{i}")
            if st.button(f"Submit ", key=f"submit_quiz_{i}"):
                if selected.lower() == quiz["answer"].lower():
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong answer. Correct: {quiz['answer']}")
    else:
        st.info("Quiz not available for this topic.")


# CLI version (for terminal interaction)
def run_cli():
    recommender = Recommender()
    topic = input("Which topic do you want to learn about? ")
    info = recommender.get_topic_info(topic)
    if info:
        print(f"\nTopic: {info['topic']}")
        print(f"Code Example:\n{info['code']}")
        print(f"Recommended YouTube Channel: {info['youtube']}")
    else:
        print("Topic not found.")
