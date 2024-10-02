package lista_dupla;

public class Node<T> {

    private T elemento;
    private Node<T> anterior;
    private Node<T> proximo;

    // Construtores
    public Node(T elemento) {
        this.elemento = elemento;
    }
    public void Node(T elemento, Node<T> anterior, Node<T> proximo) {
        this.elemento = elemento;
        this.anterior = anterior;
        this.proximo = proximo;
    }

    public T getElemento() {
        return elemento;
    }
    public void setElemento(T elemento) {
        this.elemento = elemento;
    }

    public Node<T> getAnterior() {
        return anterior;
    }

    public void setAnterior(Node<T> anterior) {
        this.anterior = anterior;
    }

    public Node<T> getProximo() {
        return proximo;
    }

    public void setProximo(Node<T> proximo) {
        this.proximo = proximo;
    }

    public String toString() {
        return "Node{" + "Element: " + this.elemento + "}";
    }
}
