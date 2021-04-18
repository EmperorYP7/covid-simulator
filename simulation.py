import matplotlib.pyplot as plt
import params
import virus


def main():
    covidparams = params.COVID19_PARAMS
    coronavirus = virus.Virus(covidparams)
    coronavirus.animate()
    plt.show()


if __name__ == "__main__":
    main()
