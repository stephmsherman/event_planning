import cairo
import pandas as pd

def write_envelopes(export_file, from_addr, to_addrs, font='Helvetica', fontsize_from_addr=8,
                    fontsize_to_addrs=14,page_width=6.25, page_height=4.25,
                    inches_to_points=72, margin=.25, horiz_align=2.25,
                    vert_align=2):
    """The purpose of this function is to export a pdf where each page is an envelope
    with a to and from address - modified: https://github.com/evmar/envelope/blob/master/envelope.py

    Parameters
    ----------
    export_file: str
        path and name of pdf to export
    from_addr : list or tuple
        The from address on each envelope
    to_addrs : list
        Nested list of addresses to mail. Each line of the address is one item in the list
    font : str
        fonts from cairo package
    fontsize_from_addr : int
        font size for from_addr
    fontsize_to_addrs : int
        font size for to_addrs
    page_width : float
        width of exported pdf
    page_height : float
        height of exported pdf
    inches_to_points : int
        inches to points conversion
    margin : float
        margin

    Returns
    -------
    pdf
    """

    surface = cairo.PDFSurface(export_file,
                               page_width * inches_to_points,
                               page_height * inches_to_points)
    cr = cairo.Context(surface)
    cr.select_font_face(font)

    for to_addr in to_addrs:
        for i, line in enumerate(from_addr):
            cr.set_font_size(fontsize_from_addr)
            cr.move_to(margin * inches_to_points,
                       (margin * inches_to_points) + fontsize_from_addr+2 + ((fontsize_from_addr+2) * i))
            cr.show_text(line)

        for i, line in enumerate(to_addr):
            cr.set_font_size(fontsize_to_addrs)
            cr.move_to(horiz_align * inches_to_points,
                       (vert_align * inches_to_points) + fontsize_to_addrs+2 + ((fontsize_to_addrs+2) * i))
            cr.show_text(line)
        cr.show_page()

    surface.flush()
    surface.finish()
