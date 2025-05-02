import streamlit as st

st.set_page_config(layout="wide")

video_html = """
		<style>

		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 100%;
		  padding: 20px;
		}

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://mega.nz/embed/gL8DVJAS#v0N4XRIu_zblleM279bd3m5zxPReKcGc7ri8qbUcHqE">
		  Your browser does not support HTML5 video.
		</video>
        """

st.markdown(video_html, unsafe_allow_html=True)
st.title('Video page')
