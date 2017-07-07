# this is to get rid of the pkg-resources package when retrieving pip's requirements
pip freeze | grep -v "pkg-resources" > requirements.txt
