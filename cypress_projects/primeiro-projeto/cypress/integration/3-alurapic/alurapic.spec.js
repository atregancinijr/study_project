describe('Usabilidades pagina inicial', () => {

    beforeEach(() => {
        cy.visit('https://alura-fotos.herokuapp.com')
    })

    it('verifica mensagens tela inicial', () => {
        cy.contains('ap-vmessage', 'User name is required!').should('be.visible');
        cy.contains('ap-vmessage', 'Password is required!').should('be.visible');
        cy.get('button[type="submit"]').should('be.disabled');
    })

    it('verifica botao habilitado na tela inicial', () => {
        cy.get('input[formcontrolname="userName"]').type('ander');
        cy.get('input[formcontrolname="password"]').type('ander123');
        cy.get('button[type=submit]').should('be.enabled');
    })

    it('verifica nome da aplicacao na tela inicial', () => {
        cy.contains('a', 'ALURAPIC').should('be.visible');
        cy.contains('h4', 'Login').should('be.visible');
    })

    it('verifica menu clicavel tela inicial', () => {
        cy.get('.navbar-brand > .fa').click();
        cy.get('.menu-bar > .fa').should('be.visible');
    })
})

