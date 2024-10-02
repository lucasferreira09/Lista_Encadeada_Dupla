package lista_dupla.test;

import lista_dupla.ListaEncadeadaDupla;

public class ListaEncadeadDuplaTest {

    public static void main(String[] args) {

        ListaEncadeadaDupla<Integer> lista = new ListaEncadeadaDupla<>();

        for (int i = 1; i <= 5; i++) {
            lista.adiciona(i);
        }

        System.out.println(lista);
    }
}
