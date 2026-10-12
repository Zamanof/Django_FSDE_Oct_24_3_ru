def paginate(
        query,
        page:int = 1,
size:int = 10,
):
    total = query.count()
    items = query.offset((page - 1)*size ).limit(size).all()

    return {
        'count':total,
        'page':page,
        'size':size,
        'results':items,
    }