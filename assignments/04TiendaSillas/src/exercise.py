# Escribe tus funciones abajo de esta línea

def main():
    # Escribe tu código abajo de esta línea
    def dsc(sil,t1):
       if c=='F':
           ds==t1*0.20
            return ds
        elif c=='N' and t1<10000:
            ds=0
            return ds
        elif c=='N' and t1>=10000 and t1<20000:
            ds=t1*0.10
            return ds
        elif c=='N' and t1>=20000:
            ds=t1*0.15
            return ds
   ts=str(input('tipo silla: '))
   c=str(input('tipo caliente: '))
    sil=int(input('cantidad de sillas: '))
    
    if ts=='B':
        ps=700
    elif ts=='E':
        ps==900
    elif ts=='L':
        ps=1500
    t1=float(sil*ps)
    print('total sin dcto. $'+str(t1))
    descuento=print('descuento          $',str(float(dsc(sil,t1))))
    disc=float(dsc(sil,t1))
    total2=print('total a pagar    $'+str(float(t1-disc)))
    

if __name__ == '__main__':
    main()
