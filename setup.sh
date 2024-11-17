mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

# Install Git LFS and set it up
apt update && apt install -y git-lfs   # Install Git LFS on Render
git lfs install                        # Initialize Git LFS
git lfs pull                           # Pull the large files tracked by LFS