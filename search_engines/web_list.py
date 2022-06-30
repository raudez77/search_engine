import numpy


def result_html(title: str, content: str):
    """ Renturn a html template (str) to adjust the number of results"""

    number = numpy.random.randint(1, 10, 1)
    web = f"""<div class="col-xs-6 col-sm-3 col-md-3 dbox prod-cnt webdesign">
         <div class="itemCont">
           <a href="#">
             <div class="thumb"><img class="img-responsive center-block" alt="Womens Stone" src="static/images_results/grids/img{int(number)}.jpg"></div>
                <div class="itemInfo">
                  <h4>{str(title)}</h4>
                          <h6>Category</h6>
                          <p>{str(content[:300])}...</p>
                        </div>
                      </a>
                      <button type="button" class="btn btn-primary goto">view</button>
                    </div>
                  </div>"""
    return web