from Chatalyzer.actions1.plotter import groupPlotter, userPlotter
from Chatalyzer.actions1.pdfmaker import add_image
import sys
from Chatalyzer.msteams.extract_to_df import getRootMessages

# if __name__ == '__main__':
#     # Map command line arguments to function arguments.
#     userPlotter(sys.argv[1])

# add_image('ax1_figure.png', 'ax2_figure.png', 'ax3_figure.png', 'ax4_figure.png')

# groupPlotter()
# add_image('ax1_figure.png', 'ax2_figure.png', 'ax3_figure.png', 'ax4_figure.png')

getRootMessages(1,2)
