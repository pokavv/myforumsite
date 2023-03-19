# myforumsite
django 2.2 forum site mini project

## 2023.03.17
- myforumsite mini project start

## 2023.03.19
1. add index.html, post-list.html, posting.html, write.html
- index.html is the home page.
post-list.html shows the post list and the page url is set to /list/.
posting.html shows one posting, and the page url of each post is set as the primary key (pk) of each post.
write.html is the writing page, and the url is requested through the "Write" button on the post-list page.
Save the new post by 'POST' to the server through the <form> tag.

2. add views : index, post_list, posting, write