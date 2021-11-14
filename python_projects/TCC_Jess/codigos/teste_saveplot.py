if __name__== "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    from datetime import datetime

    x = np.arange(0, 10, 1)
    y = np.arange(0, 10, 1)
    z = np.arange(0, 20, 2)
    aux = np.array([0, 1])
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")

    fig, (ax0, ax1) = plt.subplots(ncols=2, constrained_layout=True, sharex=True, sharey=True)
    ax0.set_aspect('equal', adjustable='box')
    ax0.set_title('teste 1')
    ax0.scatter(x, y, edgecolors='k', s=10)


    ax1.scatter(x, z, edgecolors='k', s=10)
    ax1.set_aspect('equal', adjustable='box')
    ax1.set_title('teste 2')

    plt.savefig(f'{current_time}__1.pdf')

    if np.sum(aux) > 0:
       fig, (ax2, ax3) = plt.subplots(ncols=2, constrained_layout=True, sharex=True, sharey=True)
       ax2.set_aspect('equal', adjustable='box')
       ax2.set_title('teste 3')
       ax2.scatter(z, y, edgecolors='k', s=10, c='red')

       ax3.scatter(z, x, edgecolors='k', s=10, c='red')
       ax3.set_aspect('equal', adjustable='box')
       ax3.set_title('teste 4')
       plt.savefig(f'{current_time}__2.pdf')
    else:
         pass