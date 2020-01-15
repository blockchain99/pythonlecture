def tourguide(tourist, indexnum, placetogo):
    lenth_of_list = len(placetogo)
    if indexnum  >  lenth_of_list - 1:
        raise IndexError(f" index is outof range of {placetogo} list")
    return f"Hi, {tourist} !, you choosed {placetogo[indexnum]} outof {len(placetogo)}."