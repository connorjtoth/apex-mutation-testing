# Generated from apex.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .apexParser import apexParser
else:
    from apexParser import apexParser

# This class defines a complete listener for a parse tree produced by apexParser.
class apexListener(ParseTreeListener):

    # Enter a parse tree produced by apexParser#compilationUnit.
    def enterCompilationUnit(self, ctx:apexParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by apexParser#compilationUnit.
    def exitCompilationUnit(self, ctx:apexParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by apexParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:apexParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:apexParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#importDeclaration.
    def enterImportDeclaration(self, ctx:apexParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#importDeclaration.
    def exitImportDeclaration(self, ctx:apexParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:apexParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:apexParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#modifier.
    def enterModifier(self, ctx:apexParser.ModifierContext):
        pass

    # Exit a parse tree produced by apexParser#modifier.
    def exitModifier(self, ctx:apexParser.ModifierContext):
        pass


    # Enter a parse tree produced by apexParser#classOrInterfaceModifier.
    def enterClassOrInterfaceModifier(self, ctx:apexParser.ClassOrInterfaceModifierContext):
        pass

    # Exit a parse tree produced by apexParser#classOrInterfaceModifier.
    def exitClassOrInterfaceModifier(self, ctx:apexParser.ClassOrInterfaceModifierContext):
        pass


    # Enter a parse tree produced by apexParser#variableModifier.
    def enterVariableModifier(self, ctx:apexParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by apexParser#variableModifier.
    def exitVariableModifier(self, ctx:apexParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by apexParser#classDeclaration.
    def enterClassDeclaration(self, ctx:apexParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#classDeclaration.
    def exitClassDeclaration(self, ctx:apexParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#typeParameters.
    def enterTypeParameters(self, ctx:apexParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by apexParser#typeParameters.
    def exitTypeParameters(self, ctx:apexParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by apexParser#typeParameter.
    def enterTypeParameter(self, ctx:apexParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by apexParser#typeParameter.
    def exitTypeParameter(self, ctx:apexParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by apexParser#typeBound.
    def enterTypeBound(self, ctx:apexParser.TypeBoundContext):
        pass

    # Exit a parse tree produced by apexParser#typeBound.
    def exitTypeBound(self, ctx:apexParser.TypeBoundContext):
        pass


    # Enter a parse tree produced by apexParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:apexParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:apexParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#enumConstants.
    def enterEnumConstants(self, ctx:apexParser.EnumConstantsContext):
        pass

    # Exit a parse tree produced by apexParser#enumConstants.
    def exitEnumConstants(self, ctx:apexParser.EnumConstantsContext):
        pass


    # Enter a parse tree produced by apexParser#enumConstant.
    def enterEnumConstant(self, ctx:apexParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by apexParser#enumConstant.
    def exitEnumConstant(self, ctx:apexParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by apexParser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:apexParser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by apexParser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:apexParser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by apexParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:apexParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:apexParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#typeList.
    def enterTypeList(self, ctx:apexParser.TypeListContext):
        pass

    # Exit a parse tree produced by apexParser#typeList.
    def exitTypeList(self, ctx:apexParser.TypeListContext):
        pass


    # Enter a parse tree produced by apexParser#classBody.
    def enterClassBody(self, ctx:apexParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by apexParser#classBody.
    def exitClassBody(self, ctx:apexParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by apexParser#interfaceBody.
    def enterInterfaceBody(self, ctx:apexParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by apexParser#interfaceBody.
    def exitInterfaceBody(self, ctx:apexParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by apexParser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:apexParser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:apexParser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:apexParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:apexParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:apexParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:apexParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#genericMethodDeclaration.
    def enterGenericMethodDeclaration(self, ctx:apexParser.GenericMethodDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#genericMethodDeclaration.
    def exitGenericMethodDeclaration(self, ctx:apexParser.GenericMethodDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:apexParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:apexParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#genericConstructorDeclaration.
    def enterGenericConstructorDeclaration(self, ctx:apexParser.GenericConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#genericConstructorDeclaration.
    def exitGenericConstructorDeclaration(self, ctx:apexParser.GenericConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:apexParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:apexParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#propertyDeclaration.
    def enterPropertyDeclaration(self, ctx:apexParser.PropertyDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#propertyDeclaration.
    def exitPropertyDeclaration(self, ctx:apexParser.PropertyDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#propertyBodyDeclaration.
    def enterPropertyBodyDeclaration(self, ctx:apexParser.PropertyBodyDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#propertyBodyDeclaration.
    def exitPropertyBodyDeclaration(self, ctx:apexParser.PropertyBodyDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#interfaceBodyDeclaration.
    def enterInterfaceBodyDeclaration(self, ctx:apexParser.InterfaceBodyDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#interfaceBodyDeclaration.
    def exitInterfaceBodyDeclaration(self, ctx:apexParser.InterfaceBodyDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:apexParser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:apexParser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#constDeclaration.
    def enterConstDeclaration(self, ctx:apexParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#constDeclaration.
    def exitConstDeclaration(self, ctx:apexParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#constantDeclarator.
    def enterConstantDeclarator(self, ctx:apexParser.ConstantDeclaratorContext):
        pass

    # Exit a parse tree produced by apexParser#constantDeclarator.
    def exitConstantDeclarator(self, ctx:apexParser.ConstantDeclaratorContext):
        pass


    # Enter a parse tree produced by apexParser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:apexParser.InterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#interfaceMethodDeclaration.
    def exitInterfaceMethodDeclaration(self, ctx:apexParser.InterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#genericInterfaceMethodDeclaration.
    def enterGenericInterfaceMethodDeclaration(self, ctx:apexParser.GenericInterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#genericInterfaceMethodDeclaration.
    def exitGenericInterfaceMethodDeclaration(self, ctx:apexParser.GenericInterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:apexParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by apexParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:apexParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by apexParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:apexParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by apexParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:apexParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by apexParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:apexParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by apexParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:apexParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by apexParser#variableInitializer.
    def enterVariableInitializer(self, ctx:apexParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by apexParser#variableInitializer.
    def exitVariableInitializer(self, ctx:apexParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by apexParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:apexParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by apexParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:apexParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by apexParser#enumConstantName.
    def enterEnumConstantName(self, ctx:apexParser.EnumConstantNameContext):
        pass

    # Exit a parse tree produced by apexParser#enumConstantName.
    def exitEnumConstantName(self, ctx:apexParser.EnumConstantNameContext):
        pass


    # Enter a parse tree produced by apexParser#typeType.
    def enterTypeType(self, ctx:apexParser.TypeTypeContext):
        pass

    # Exit a parse tree produced by apexParser#typeType.
    def exitTypeType(self, ctx:apexParser.TypeTypeContext):
        pass


    # Enter a parse tree produced by apexParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:apexParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by apexParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:apexParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by apexParser#primitiveType.
    def enterPrimitiveType(self, ctx:apexParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by apexParser#primitiveType.
    def exitPrimitiveType(self, ctx:apexParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by apexParser#typeArguments.
    def enterTypeArguments(self, ctx:apexParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by apexParser#typeArguments.
    def exitTypeArguments(self, ctx:apexParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by apexParser#typeArgument.
    def enterTypeArgument(self, ctx:apexParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by apexParser#typeArgument.
    def exitTypeArgument(self, ctx:apexParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by apexParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:apexParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by apexParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:apexParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by apexParser#formalParameters.
    def enterFormalParameters(self, ctx:apexParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by apexParser#formalParameters.
    def exitFormalParameters(self, ctx:apexParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by apexParser#formalParameterList.
    def enterFormalParameterList(self, ctx:apexParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by apexParser#formalParameterList.
    def exitFormalParameterList(self, ctx:apexParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by apexParser#formalParameter.
    def enterFormalParameter(self, ctx:apexParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by apexParser#formalParameter.
    def exitFormalParameter(self, ctx:apexParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by apexParser#lastFormalParameter.
    def enterLastFormalParameter(self, ctx:apexParser.LastFormalParameterContext):
        pass

    # Exit a parse tree produced by apexParser#lastFormalParameter.
    def exitLastFormalParameter(self, ctx:apexParser.LastFormalParameterContext):
        pass


    # Enter a parse tree produced by apexParser#methodBody.
    def enterMethodBody(self, ctx:apexParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by apexParser#methodBody.
    def exitMethodBody(self, ctx:apexParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by apexParser#constructorBody.
    def enterConstructorBody(self, ctx:apexParser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by apexParser#constructorBody.
    def exitConstructorBody(self, ctx:apexParser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by apexParser#qualifiedName.
    def enterQualifiedName(self, ctx:apexParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by apexParser#qualifiedName.
    def exitQualifiedName(self, ctx:apexParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by apexParser#literal.
    def enterLiteral(self, ctx:apexParser.LiteralContext):
        pass

    # Exit a parse tree produced by apexParser#literal.
    def exitLiteral(self, ctx:apexParser.LiteralContext):
        pass


    # Enter a parse tree produced by apexParser#annotation.
    def enterAnnotation(self, ctx:apexParser.AnnotationContext):
        pass

    # Exit a parse tree produced by apexParser#annotation.
    def exitAnnotation(self, ctx:apexParser.AnnotationContext):
        pass


    # Enter a parse tree produced by apexParser#annotationName.
    def enterAnnotationName(self, ctx:apexParser.AnnotationNameContext):
        pass

    # Exit a parse tree produced by apexParser#annotationName.
    def exitAnnotationName(self, ctx:apexParser.AnnotationNameContext):
        pass


    # Enter a parse tree produced by apexParser#elementValuePairs.
    def enterElementValuePairs(self, ctx:apexParser.ElementValuePairsContext):
        pass

    # Exit a parse tree produced by apexParser#elementValuePairs.
    def exitElementValuePairs(self, ctx:apexParser.ElementValuePairsContext):
        pass


    # Enter a parse tree produced by apexParser#elementValuePair.
    def enterElementValuePair(self, ctx:apexParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by apexParser#elementValuePair.
    def exitElementValuePair(self, ctx:apexParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by apexParser#elementValue.
    def enterElementValue(self, ctx:apexParser.ElementValueContext):
        pass

    # Exit a parse tree produced by apexParser#elementValue.
    def exitElementValue(self, ctx:apexParser.ElementValueContext):
        pass


    # Enter a parse tree produced by apexParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:apexParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by apexParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:apexParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by apexParser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:apexParser.AnnotationTypeDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#annotationTypeDeclaration.
    def exitAnnotationTypeDeclaration(self, ctx:apexParser.AnnotationTypeDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:apexParser.AnnotationTypeBodyContext):
        pass

    # Exit a parse tree produced by apexParser#annotationTypeBody.
    def exitAnnotationTypeBody(self, ctx:apexParser.AnnotationTypeBodyContext):
        pass


    # Enter a parse tree produced by apexParser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:apexParser.AnnotationTypeElementDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#annotationTypeElementDeclaration.
    def exitAnnotationTypeElementDeclaration(self, ctx:apexParser.AnnotationTypeElementDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#annotationTypeElementRest.
    def enterAnnotationTypeElementRest(self, ctx:apexParser.AnnotationTypeElementRestContext):
        pass

    # Exit a parse tree produced by apexParser#annotationTypeElementRest.
    def exitAnnotationTypeElementRest(self, ctx:apexParser.AnnotationTypeElementRestContext):
        pass


    # Enter a parse tree produced by apexParser#annotationMethodOrConstantRest.
    def enterAnnotationMethodOrConstantRest(self, ctx:apexParser.AnnotationMethodOrConstantRestContext):
        pass

    # Exit a parse tree produced by apexParser#annotationMethodOrConstantRest.
    def exitAnnotationMethodOrConstantRest(self, ctx:apexParser.AnnotationMethodOrConstantRestContext):
        pass


    # Enter a parse tree produced by apexParser#annotationMethodRest.
    def enterAnnotationMethodRest(self, ctx:apexParser.AnnotationMethodRestContext):
        pass

    # Exit a parse tree produced by apexParser#annotationMethodRest.
    def exitAnnotationMethodRest(self, ctx:apexParser.AnnotationMethodRestContext):
        pass


    # Enter a parse tree produced by apexParser#annotationConstantRest.
    def enterAnnotationConstantRest(self, ctx:apexParser.AnnotationConstantRestContext):
        pass

    # Exit a parse tree produced by apexParser#annotationConstantRest.
    def exitAnnotationConstantRest(self, ctx:apexParser.AnnotationConstantRestContext):
        pass


    # Enter a parse tree produced by apexParser#defaultValue.
    def enterDefaultValue(self, ctx:apexParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by apexParser#defaultValue.
    def exitDefaultValue(self, ctx:apexParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by apexParser#block.
    def enterBlock(self, ctx:apexParser.BlockContext):
        pass

    # Exit a parse tree produced by apexParser#block.
    def exitBlock(self, ctx:apexParser.BlockContext):
        pass


    # Enter a parse tree produced by apexParser#blockStatement.
    def enterBlockStatement(self, ctx:apexParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by apexParser#blockStatement.
    def exitBlockStatement(self, ctx:apexParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by apexParser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:apexParser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by apexParser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:apexParser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by apexParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:apexParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by apexParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:apexParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by apexParser#statement.
    def enterStatement(self, ctx:apexParser.StatementContext):
        pass

    # Exit a parse tree produced by apexParser#statement.
    def exitStatement(self, ctx:apexParser.StatementContext):
        pass


    # Enter a parse tree produced by apexParser#propertyBlock.
    def enterPropertyBlock(self, ctx:apexParser.PropertyBlockContext):
        pass

    # Exit a parse tree produced by apexParser#propertyBlock.
    def exitPropertyBlock(self, ctx:apexParser.PropertyBlockContext):
        pass


    # Enter a parse tree produced by apexParser#getter.
    def enterGetter(self, ctx:apexParser.GetterContext):
        pass

    # Exit a parse tree produced by apexParser#getter.
    def exitGetter(self, ctx:apexParser.GetterContext):
        pass


    # Enter a parse tree produced by apexParser#setter.
    def enterSetter(self, ctx:apexParser.SetterContext):
        pass

    # Exit a parse tree produced by apexParser#setter.
    def exitSetter(self, ctx:apexParser.SetterContext):
        pass


    # Enter a parse tree produced by apexParser#catchClause.
    def enterCatchClause(self, ctx:apexParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by apexParser#catchClause.
    def exitCatchClause(self, ctx:apexParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by apexParser#catchType.
    def enterCatchType(self, ctx:apexParser.CatchTypeContext):
        pass

    # Exit a parse tree produced by apexParser#catchType.
    def exitCatchType(self, ctx:apexParser.CatchTypeContext):
        pass


    # Enter a parse tree produced by apexParser#finallyBlock.
    def enterFinallyBlock(self, ctx:apexParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by apexParser#finallyBlock.
    def exitFinallyBlock(self, ctx:apexParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by apexParser#resourceSpecification.
    def enterResourceSpecification(self, ctx:apexParser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by apexParser#resourceSpecification.
    def exitResourceSpecification(self, ctx:apexParser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by apexParser#resources.
    def enterResources(self, ctx:apexParser.ResourcesContext):
        pass

    # Exit a parse tree produced by apexParser#resources.
    def exitResources(self, ctx:apexParser.ResourcesContext):
        pass


    # Enter a parse tree produced by apexParser#resource.
    def enterResource(self, ctx:apexParser.ResourceContext):
        pass

    # Exit a parse tree produced by apexParser#resource.
    def exitResource(self, ctx:apexParser.ResourceContext):
        pass


    # Enter a parse tree produced by apexParser#forControl.
    def enterForControl(self, ctx:apexParser.ForControlContext):
        pass

    # Exit a parse tree produced by apexParser#forControl.
    def exitForControl(self, ctx:apexParser.ForControlContext):
        pass


    # Enter a parse tree produced by apexParser#forInit.
    def enterForInit(self, ctx:apexParser.ForInitContext):
        pass

    # Exit a parse tree produced by apexParser#forInit.
    def exitForInit(self, ctx:apexParser.ForInitContext):
        pass


    # Enter a parse tree produced by apexParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:apexParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by apexParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:apexParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by apexParser#forUpdate.
    def enterForUpdate(self, ctx:apexParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by apexParser#forUpdate.
    def exitForUpdate(self, ctx:apexParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by apexParser#parExpression.
    def enterParExpression(self, ctx:apexParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by apexParser#parExpression.
    def exitParExpression(self, ctx:apexParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by apexParser#expressionList.
    def enterExpressionList(self, ctx:apexParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by apexParser#expressionList.
    def exitExpressionList(self, ctx:apexParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by apexParser#statementExpression.
    def enterStatementExpression(self, ctx:apexParser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by apexParser#statementExpression.
    def exitStatementExpression(self, ctx:apexParser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by apexParser#constantExpression.
    def enterConstantExpression(self, ctx:apexParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by apexParser#constantExpression.
    def exitConstantExpression(self, ctx:apexParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by apexParser#apexDbUpsertExpression.
    def enterApexDbUpsertExpression(self, ctx:apexParser.ApexDbUpsertExpressionContext):
        pass

    # Exit a parse tree produced by apexParser#apexDbUpsertExpression.
    def exitApexDbUpsertExpression(self, ctx:apexParser.ApexDbUpsertExpressionContext):
        pass


    # Enter a parse tree produced by apexParser#apexDbExpression.
    def enterApexDbExpression(self, ctx:apexParser.ApexDbExpressionContext):
        pass

    # Exit a parse tree produced by apexParser#apexDbExpression.
    def exitApexDbExpression(self, ctx:apexParser.ApexDbExpressionContext):
        pass


    # Enter a parse tree produced by apexParser#expression.
    def enterExpression(self, ctx:apexParser.ExpressionContext):
        pass

    # Exit a parse tree produced by apexParser#expression.
    def exitExpression(self, ctx:apexParser.ExpressionContext):
        pass


    # Enter a parse tree produced by apexParser#primary.
    def enterPrimary(self, ctx:apexParser.PrimaryContext):
        pass

    # Exit a parse tree produced by apexParser#primary.
    def exitPrimary(self, ctx:apexParser.PrimaryContext):
        pass


    # Enter a parse tree produced by apexParser#creator.
    def enterCreator(self, ctx:apexParser.CreatorContext):
        pass

    # Exit a parse tree produced by apexParser#creator.
    def exitCreator(self, ctx:apexParser.CreatorContext):
        pass


    # Enter a parse tree produced by apexParser#createdName.
    def enterCreatedName(self, ctx:apexParser.CreatedNameContext):
        pass

    # Exit a parse tree produced by apexParser#createdName.
    def exitCreatedName(self, ctx:apexParser.CreatedNameContext):
        pass


    # Enter a parse tree produced by apexParser#innerCreator.
    def enterInnerCreator(self, ctx:apexParser.InnerCreatorContext):
        pass

    # Exit a parse tree produced by apexParser#innerCreator.
    def exitInnerCreator(self, ctx:apexParser.InnerCreatorContext):
        pass


    # Enter a parse tree produced by apexParser#arrayCreatorRest.
    def enterArrayCreatorRest(self, ctx:apexParser.ArrayCreatorRestContext):
        pass

    # Exit a parse tree produced by apexParser#arrayCreatorRest.
    def exitArrayCreatorRest(self, ctx:apexParser.ArrayCreatorRestContext):
        pass


    # Enter a parse tree produced by apexParser#mapCreatorRest.
    def enterMapCreatorRest(self, ctx:apexParser.MapCreatorRestContext):
        pass

    # Exit a parse tree produced by apexParser#mapCreatorRest.
    def exitMapCreatorRest(self, ctx:apexParser.MapCreatorRestContext):
        pass


    # Enter a parse tree produced by apexParser#setCreatorRest.
    def enterSetCreatorRest(self, ctx:apexParser.SetCreatorRestContext):
        pass

    # Exit a parse tree produced by apexParser#setCreatorRest.
    def exitSetCreatorRest(self, ctx:apexParser.SetCreatorRestContext):
        pass


    # Enter a parse tree produced by apexParser#classCreatorRest.
    def enterClassCreatorRest(self, ctx:apexParser.ClassCreatorRestContext):
        pass

    # Exit a parse tree produced by apexParser#classCreatorRest.
    def exitClassCreatorRest(self, ctx:apexParser.ClassCreatorRestContext):
        pass


    # Enter a parse tree produced by apexParser#explicitGenericInvocation.
    def enterExplicitGenericInvocation(self, ctx:apexParser.ExplicitGenericInvocationContext):
        pass

    # Exit a parse tree produced by apexParser#explicitGenericInvocation.
    def exitExplicitGenericInvocation(self, ctx:apexParser.ExplicitGenericInvocationContext):
        pass


    # Enter a parse tree produced by apexParser#nonWildcardTypeArguments.
    def enterNonWildcardTypeArguments(self, ctx:apexParser.NonWildcardTypeArgumentsContext):
        pass

    # Exit a parse tree produced by apexParser#nonWildcardTypeArguments.
    def exitNonWildcardTypeArguments(self, ctx:apexParser.NonWildcardTypeArgumentsContext):
        pass


    # Enter a parse tree produced by apexParser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:apexParser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by apexParser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:apexParser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by apexParser#nonWildcardTypeArgumentsOrDiamond.
    def enterNonWildcardTypeArgumentsOrDiamond(self, ctx:apexParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by apexParser#nonWildcardTypeArgumentsOrDiamond.
    def exitNonWildcardTypeArgumentsOrDiamond(self, ctx:apexParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by apexParser#superSuffix.
    def enterSuperSuffix(self, ctx:apexParser.SuperSuffixContext):
        pass

    # Exit a parse tree produced by apexParser#superSuffix.
    def exitSuperSuffix(self, ctx:apexParser.SuperSuffixContext):
        pass


    # Enter a parse tree produced by apexParser#explicitGenericInvocationSuffix.
    def enterExplicitGenericInvocationSuffix(self, ctx:apexParser.ExplicitGenericInvocationSuffixContext):
        pass

    # Exit a parse tree produced by apexParser#explicitGenericInvocationSuffix.
    def exitExplicitGenericInvocationSuffix(self, ctx:apexParser.ExplicitGenericInvocationSuffixContext):
        pass


    # Enter a parse tree produced by apexParser#arguments.
    def enterArguments(self, ctx:apexParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by apexParser#arguments.
    def exitArguments(self, ctx:apexParser.ArgumentsContext):
        pass


