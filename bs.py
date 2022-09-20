# @ig.route('/mycart')  show cart
# def getAllPosts():
#     posts = Cart.query.all()
#     print(posts)
#     return render_template('feed.html', posts=posts)


# @ig.route('/mycart/update/<int:post_id>', methods=['GET','POST']) # dynamic route
# def updatePost(post_id):
#     form = PostForm()
#     post = Post.query.get(post_id)
#     if current_user.id != post.user_id:
#         flash('You are not allowed to update another user\'s post', category='danger')
#         return redirect(url_for('ig.singlePost', post_id=post_id))
#     if request.method == 'POST':
#         if form.validate():
#             title = form.title.data
#             img_url = form.img_url.data
#             caption = form.caption.data

#             # update post from database
#             post.title = title
#             post.img_url = img_url
#             post.caption = caption

#             db.session.commit()
#             flash('Successfully updated post.', category='success')
#             return redirect(url_for('ig.singlePost', post_id=post_id))
#         else:
#             flash('Invalid form, please check input fields!', category='danger')
#     return render_template('updatePost.html', form=form, post=post)




# @ig.route('/mycart/add', methods=['GET', 'POST'])
# @login_required
# def createCart():
#     form = CartForm()
#     if request.method == 'POST':
#         if form.validate():
#             title = form.title.data
#             img_url = form.img_url.data
#             caption = form.caption.data

#             # add post to database
#             cart = Cart(title, img_url, caption, current_user.id)

#             # add instance to database
#             db.session.add(cart)
#             db.session.commit()

#             flash('Successfully created post.', category='success')
#         else:
#             flash('Invalid form, please check input fields!', category='danger')


#     return render_template('cart.html', form=form)