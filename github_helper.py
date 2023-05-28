from github.MainClass import Github


class GithubHelper:

    # Read the access token from the file
    def read_access_token(self):
        with open('../config.txt', 'r') as file:
            access_tok = file.read().strip()
            #print(access_tok)
        return access_tok

    def get_github_object(self):
        # Read the access token from the file
        access_token = self.read_access_token()

        # Initialize GitHub object
        g = Github(access_token)
        return g

    def get_sha(self, repo_name, file_name):
        # Get the repository
        g = self.get_github_object()
        repo = g.get_user().get_repo(repo_name)
        file_contents = repo.get_contents(file_name)
        return file_contents.sha

    def create_file(self, repo_name, file_name, commit_message, content, sha=None):
        # Get the repository
        g = self.get_github_object()
        repo = g.get_user().get_repo(repo_name)
        if sha:
            # Update the file
            repo.update_file(file_name, commit_message, content, sha)
        else:
            # Upload the file to the repository
            repo.create_file(file_name, commit_message, content)
