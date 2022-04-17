describe('Login de usuários alura pic', () => {

    beforeEach(() => {
        cy.visit('https://alura-fotos.herokuapp.com')
        cy.intercept('POST', 'https://apialurapic.herokuapp.com/user/login', {
            statusCode: 400
        }).as('stubPost')

    })
    
    it.only('fazer login de usuario valido', () => {
        cy.login(Cypress.env('userName'), Cypress.env('password'))
        //cy.wait('@stubPost') //aguarda stubPost criado acima -> desmomentar para usar
        cy.contains('a', '(Logout)').should('be.visible')

    })

    it('fazer login de usuario invalido', () => {
        cy.login('anderson', '4321')
        cy.on('window:alert', (str) => {
            expect(str).to.equal('Invalid user name or password')
        }) 
    })
    
    
})