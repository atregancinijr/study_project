describe('Cadastro de usuários alura pic', () => {

    beforeEach(() => {
        cy.visit('/')
    })

    it('verifica mensagens validacao', () => {
        cy.contains('a','Register now').click();
        cy.contains('button', 'Register').click().click();
        cy.contains('ap-vmessage', 'Email is required!').should('be.visible');
        cy.contains('ap-vmessage', 'Full name is required!').should('be.visible');
        cy.contains('ap-vmessage', 'User name is required!').should('be.visible');
        cy.contains('ap-vmessage', 'Password is required!').should('be.visible');
    })

    it('verifica mensagem de e-mail invalido', () => {
        cy.contains('a','Register now').click();
        cy.get('input[formcontrolname="email"]').type('anderson');
        cy.contains('button', 'Register').click().click();
        cy.contains('ap-vmessage', 'Invalid e-mail').should('be.visible');
        
    })

    it('verifica mensagem de senha com menos de 8 caracteres', () => {
        cy.contains('a','Register now').click();
        cy.get('input[formcontrolname="password"]').type('123');
        cy.contains('button', 'Register').click().click();
        cy.contains('ap-vmessage', 'Mininum length is 8').should('be.visible');
        
    })

    it('verifica mensagem de user name com letra maiuscula', () => {
        cy.contains('a','Register now').click();
        cy.get('input[formcontrolname="userName"]').type('Atjunior');
        cy.contains('button', 'Register').click().click();
        cy.contains('ap-vmessage', 'Must be lower case').should('be.visible');
        
    })

    const usuarios = require('../../fixtures/usuarios.json');
    usuarios.forEach(usuario => {
        it(`registra novo usuario ${usuario.username}` , () => {
            cy.registra(usuario.email, usuario.fullname, usuario.username, usuario.password);
        })
    })

})