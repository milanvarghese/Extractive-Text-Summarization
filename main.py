import streamlit as st
import summarizer

st.title("Text Summarization")

sentence = st.text_area('Input your sentence here:', "Growing up in Canada with a life-long fascination for Canadian geography, I have always been interested in returning to the country. Although my family moved to the US before I entered high school, I have always kept my eyes turned north, especially in recent years as I began to read journal articles about research conducted on John Evans Glacier, located about 80 N latitude. Graduating next semester with a B.S. in computer science and engineering and a minor in geographic information systems, I am interested in attending the University of Alberta for graduate study. Geographic information systems (GIS) is a field especially suited to investigating spatial patterns, modeling diverse scenarios, and overlaying spatial data. This semester, in my advanced GIS course, Spatial Data Structures and Algorithms, I am part of a team developing a temporal database and program for tracing historical trading data. My computer science skills have also been put to use in two summer internship projects, where I acquired profiency with using LIDAR (light detection and ranging) technology, now favored by NASA in its current 10-year study of Greenland and changes in the ice cap extent. Through my coursework and project experience, I have also accrued skills in using Arc/Info, ArcView, Microstation, and RDBMS software packages, and I am equally comfortable programming in Visual Basic, C++, and Java. For my graduate research project, I would like to investigate methods for improving current GIS data models to better incorporate time as a variable in studying climate change. Changes in glaciers and polar environments occur rapidly, and these changes become important indicators of broader, potentially catastrophic, global changes. By developing and applying temporal GIS methods to glaciology, I can contribute to improved spatio-temporal analysis techniques for studying the polar environment and glaciers. Also, I can discern which temporal methods serve  as the best predictors and provide benefits to the GIS research community that apply to areas other than glaciology.My long-term goals are to enter the GIS field as a consultant or to extend my research and earn my Ph.D. at a program of international reputation. Having advanced experience with temporal GIS technology would make me a valuable consultant to a company, especially in the twin burgeoning fields of computer science and GIS. In applying to the University of Alberta, I recognize your strengths in both computer science and glaciology, and the recent application of these areas to field research at Ellesmere Island in Nunavut, Canada, is especially appealing to me. With my deep-rooted interest in Canadian geology and recognition of the quality of your university programs, I hope you will give my application every consideration.")

count = st.slider("Select the max number of paragraphs", 1, 5, 3)

result = st.button("Summarize")

if result==True:
    sum = summarizer.generate_summary(sentence, count)
    st.write("Summary: ")
    st.write(". ".join(sum)+".")

