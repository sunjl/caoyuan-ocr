from flask_paginate import Pagination, get_page_args

@search.route('/retrieve_data')
def retrieve():
    # get_page_arg defaults to page 1, per_page of 10
    page, per_page, offset = get_page_args()

    # After the main query, you need to apply the per_page limit and offset
    fs = gridfs.GridFS(db)
    fs_for_render = fs.limit(per_page).offset(offset)

    #you can also add css_framework='bootstrap3' to Pagination for easy styling
    pagination = Pagination(page=page, per_page=per_page, offset=offset,
                            total=fs.count(), record_name='List')

    return render_template('retrieveFile.html', fs=fs_for_render, pagination=pagination,
                           form="submitIt")