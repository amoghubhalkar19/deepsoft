import utils
import streamlit as st
import streamlit.components.v1 as comps


def git_commit_push(repo_path, commit_message):
            try:
        # Change directory to the repository path
                # subprocess.run(["cd", repo_path], check=True)

        # Stage all changes
                subprocess.run(["git", "add", "-A"], check=True)

        # Commit changes with the provided commit message
                subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push changes to the remote repository
                subprocess.run(["git", "push"], check=True)

                print("Changes committed and pushed successfully.")

            except subprocess.CalledProcessError as e:
                print("Failed to commit and push changes.")
                print(f"Error: {e}")


def main():
    st.title('Website Builder')
    user_text = st.text_input("Enter text:", "")
    
    if user_text:
        st.write("You entered:", user_text)
        code=utils.generate_code(user_text)
        utils.write_to_file(code)
        utils.git_commit_push("D:\deepsoft", "changing index.html for current input")
        website_url=utils.deploy_render_api()
        
        comps.iframe(website_url, height=500, scrolling=True)
        st.text(f'Hosted Link: {website_url}')

if __name__ == "__main__":
    main()
