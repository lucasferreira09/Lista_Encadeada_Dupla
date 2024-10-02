package lista_dupla;

public class ListaEncadeadaDupla<T> {

    private Node<T> head;
    private Node<T> tail;
    private int tamanho;


    // Adiciona no final da Lista
    public void adiciona(T elemento) {
        Node<T> node = new Node<>(elemento);

        if (this.head == null) {
            this.head = node;
            this.tail = node;
        } else {
            node.setAnterior(this.tail);
            this.tail.setProximo(node);
            this.tail = node;
        }
        this.tamanho++;
    }

    // Adiciona no Início da lista
    public void adicionaInicio(T elemento) {
        Node<T> novoNode = new Node<>(elemento);

        if (this.head == null) {
            this.head = novoNode;
            this.tail = novoNode;
        } else {
            novoNode.setProximo(this.head);
            this.head.setAnterior(novoNode);
            this.head = novoNode;
        }
        this.tamanho++;
    }

    // Adiciona em uma posição específica
    public void adiciona(int index, T elemento) {
        if (index < 0 || index > this.tamanho) {
            throw new IndexOutOfBoundsException();
        }

        Node<T> novoNode = new Node<>(elemento);

        if (index == 0) { // Adiciona no início
            this.adicionaInicio(elemento);

        } else if (index == this.tamanho) { // Adiciona no Final
            this.adiciona(elemento);

        } else { // Adiciona no Meio
            Node<T> node = this.getNode(index - 1);
            Node<T> proximo = node.getProximo();

            proximo.setAnterior(novoNode);
            novoNode.setProximo(proximo);
            novoNode.setAnterior(node);
            node.setProximo(novoNode);

            this.tamanho++;
        }
    }

    // Somente a classe pode acessar esse método, retorna o Node
    private Node<T> getNode(int index) {
        if (index < 0 || index >= this.tamanho) {
            throw new IndexOutOfBoundsException();
        }

        Node<T> node = this.head;
        for (int i = 0; i < index; i++) {
            node = node.getProximo();
        }
        return node;
    }

    // Troca o elemento no Índice dado
    public void setValue(int index, T elemento) {
        if (this.tamanho == 0) {
            throw new RuntimeException("Lista Vazia");
        }
        if (index < 0 || index >= this.tamanho) {
            throw new IndexOutOfBoundsException("Índice Inválido!");
        }

        Node<T> node = this.getNode(index);
        node.setElemento(elemento);

    }

    // Verifica se um determinado elemento está na lista
    // Retornando True ou False
    public boolean contains(T elemento) {
        if (this.tamanho == 0) {
            return false;
        }

        Node<T> node = this.head;
        while (node != null) {
            if (node.getElemento().equals(elemento)) {
                return true;
            }
            node = node.getProximo();
        }
        return false;
    }


    // Retorna True se o Primeiro elemento for removido
    public Boolean removeInicio() {
        if (this.tamanho == 0) {
            throw new RuntimeException("A Lista está vazia");
        }

        this.head = this.head.getProximo();
        this.head.setAnterior(null);
        this.tamanho--;

        if (this.tamanho == 0) {  // Depois de removido. Se o tamanho = 0
            this.tail = null;     // Removemos a referência do Node Final
        }
        return true;
    }


    // Retorna True se o elemento Final for removido
    public Boolean removeFinal() {
        if (this.tamanho == 0) {
            throw new RuntimeException("A Lista está vazia");
        }


        Node<T> node = this.getNode(this.tamanho - 2); // Para antes do elemento Final da lista

        node.setProximo(null);
        this.tail = node;
        this.tamanho--;

        return true;
    }

    // Remove o elemento de qualquer posição
    public void remove(int index) {
        if (this.tamanho == 0) {
            throw new RuntimeException("A Lista está vazia");
        }
        if (index < 0 || index >= this.tamanho) {
            throw new IndexOutOfBoundsException("Índice Inválido!");
        }

        if (index == 0) { // Remove do início
            this.removeInicio();
        } else if (index == this.tamanho - 1) { // Remove do Final
            this.removeFinal();
        } else { // Remove do meio

            Node<T> nodeAtual = this.getNode(index-1); // Para um índice antes do Node escolhido

            Node<T> proximo = nodeAtual.getProximo().getProximo();
            proximo.setAnterior(nodeAtual);
            nodeAtual.setProximo(proximo);
            this.tamanho--;

        }
    }
    public void limparLista() {
        if (this.tamanho == 0) {
            return;
        }

        Node<T> node = this.head;
        while (node != null) {
            Node<T> nextNode = node.getProximo(); // Armazena a referência do proximo, para não perder o resto da lista

            node.setElemento(null);    // É preciso percorrer a lista, e excluir cada elemento
            node.setAnterior(null);    // Por causa do Garbage Collector
            node.setProximo(null);

            node = nextNode;
        }
        this.head = null;
        this.tail = null;
        this.tamanho = 0;
    }

    // Inverte toda a lista
    public void invert() {
        if (this.tamanho == 0 || this.tamanho == 1) {
            return;
        }

        ListaEncadeadaDupla<T> novaLista = new ListaEncadeadaDupla<>();
        Node<T> node = this.tail;

        while (node != null) {
            novaLista.adiciona(node.getElemento());
            node = node.getAnterior();
        }
        this.head = novaLista.head;
        this.tail = novaLista.tail;

    }

    // Retorna o elemento, se o índice for válido
    public T getElemento(int index) {
        if (index >= this.tamanho || index < 0) {
            throw new IndexOutOfBoundsException();
        }

        Node<T> node = this.getNode(index);
        return node.getElemento();
    }


    // Retorna o índice do elemento, se ele estiver na lista
    public int getIndex(T elemento) {

        int index = 0;
        Node<T> node = this.head;

        while (node != null) {
            if (node.getElemento().equals(elemento)) {
                return index;
            }
            index++;
            node = node.getProximo();
        }
        return -1;
    }

    public int getTamanho() {
        return this.tamanho;
    }

    public String toString() {
        if (this.tamanho == 0) {
            return "[]";
        }

        StringBuilder builder = new StringBuilder("[");

        Node<T> node = this.head;
        while (node.getProximo() != null) {
            builder.append(node.getElemento()).append(",");
            node = node.getProximo();
        }
        builder.append(node.getElemento()).append("]");

        return builder.toString();
    }
}
